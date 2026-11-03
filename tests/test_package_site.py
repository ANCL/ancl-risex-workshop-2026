import importlib.util
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location('package_site', Path(__file__).parents[1] / 'scripts/package_site.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class PackageSiteTests(unittest.TestCase):
    def test_copies_site_exactly_and_excludes_private_repository_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'source'
            source.mkdir()
            (source / 'index.html').write_bytes(b'<h1>Original main site</h1>')
            (source / 'about.html').write_bytes(b'About')
            (source / 'style.css').write_bytes(b'body { color: green; }')
            (source / 'assets').mkdir()
            (source / 'assets/demo.gif').write_bytes(b'GIF89a')
            (source / '.env').write_text('not public')
            (source / 'README.md').write_text('not website content')
            (source / '.git').mkdir()
            (source / '.git/config').write_text('not public')
            output = root / 'output'
            module.package_site(source, output)
            self.assertEqual((output / 'index.html').read_bytes(), (source / 'index.html').read_bytes())
            self.assertEqual((output / 'assets/demo.gif').read_bytes(), b'GIF89a')
            self.assertEqual({p.name for p in output.iterdir()}, {'index.html','about.html','style.css','assets','.nojekyll'})

    def test_refuses_to_overwrite_existing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'index.html').touch()
            with self.assertRaises(ValueError):
                module.package_site(root, root)

    def test_rejects_symlinks_before_copying(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / 'source'
            source.mkdir()
            (source / 'index.html').touch()
            (root / 'private.txt').write_text('not public')
            try:
                (source / 'linked.html').symlink_to(root / 'private.txt')
            except OSError:
                self.skipTest('OS requires additional permission to create symlinks')
            with self.assertRaises(ValueError):
                module.package_site(source, root / 'output')
            self.assertFalse((root / 'output').exists())


if __name__ == '__main__':
    unittest.main()

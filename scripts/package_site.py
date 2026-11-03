"""Copy only public static site files; never execute code from a PR."""
from pathlib import Path
import shutil
import sys


def package_site(source: Path, destination: Path) -> None:
    source = source.resolve()
    destination = destination.resolve()
    if destination.exists():
        raise ValueError('Destination must not already exist')
    selected = [p for p in source.iterdir() if p.suffix in {'.html', '.css', '.js'} or p.name == 'assets']
    if not (source / 'index.html').is_file():
        raise ValueError('Site must contain index.html')
    for path in selected:
        entries = [path, *path.rglob('*')] if path.is_dir() else [path]
        if any(p.is_symlink() for p in entries):
            raise ValueError('Site files must not contain symlinks')
    destination.mkdir(parents=True)
    for path in selected:
        target = destination / path.name
        if path.is_dir():
            shutil.copytree(path, target)
        else:
            shutil.copy2(path, target)
    (destination / '.nojekyll').touch()


if __name__ == '__main__':
    package_site(Path(sys.argv[1]), Path(sys.argv[2]))

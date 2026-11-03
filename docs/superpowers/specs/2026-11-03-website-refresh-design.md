# Workshop website refresh

The user approved both browser previews and requested that the result be pushed to a new branch of the existing repository.

## Intent and scope

Make the workshop easier to read while preserving its identity and the existing two-page, dependency-free site. Retain every biography verbatim, all portraits, both drone demonstrations, event facts, registration destination, and contact information.

## Agreed design

- White backgrounds, dark text, and strong green accents; retain Inter.
- Responsive pages centred within a 1,280px maximum width, with modest edge padding.
- Identical responsive title size and weight on both pages; one line on desktop and natural wrapping on phones.
- A larger static ANCL mark, taken from the final frame of the existing animation, beside the lab's name.
- Home: introduction, registration and event facts, demonstrations, workshop highlights, full biographies, contact details.
- Biographies use the available text-column width and justified alignment on desktop; left alignment on narrow screens.
- About: larger body text, openly visible agenda bullets, relevant documentation links, brief ROS 2/PX4 explanations, concise outcomes, and registration.
- About subtitle: “A short talk, a guided simulation, and a real flight.”
- Programme durations: Presentation 40 minutes, Simulation 20 minutes, Real flight 30 minutes, totalling the scheduled 90 minutes.

## Approaches considered

Visual polish alone would leave repetition and weak hierarchy. The selected careful refresh improves layout and non-biographical copy while keeping the original site's identity and content. A dark first mockup was rejected for remaining muted; a light version was approved. Unbounded page width was tried and rejected; 1,280px is the approved compromise.

## Implementation constraints

Use local assets and relative page links, not preview localhost addresses or preview CDN image URLs. Keep the site deployable on GitHub Pages without a build step. Preserve responsive reflow and keyboard-visible focus. No redesign of the logo artwork, fabricated prerequisites, framework migration, main-branch merge, or deployment is included.

## Validation

Compare biography text directly against the original Git revision. Check local links, images, document structure, and absence of preview runtime code. Inspect desktop and phone layouts and exercise navigation. Push only the new branch after verification.

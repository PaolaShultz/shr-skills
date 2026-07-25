# Anonymous layered inputs

The four opaque labels are Ember, Harbor, Quartz, and Willow. Evaluators did not
receive the mapping until every valid output was frozen.

Evidence visibility was staged:

| Stage | Visible evidence |
|---|---|
| Layer 1 | `written-design.md` only |
| Layer 2 | written design plus `image-chain/` |
| Layer 3 | Layer 2 plus final image and the one intermediate image where present |
| Layer 4 | package response, image chain, delivery trace, final image, and intermediate image where present |
| Layer 5 | package response and final image |

`written-design.md` removes only image embeds and links. `package-response.md`
normalizes disposable image links to `final-image.png`. The blind image-chain
copies normalize method-revealing disposable paths; verbatim prompt text and
call order remain unchanged. Exact unnormalized provenance remains in
[`../image-instruction-chains/`](../image-instruction-chains/).

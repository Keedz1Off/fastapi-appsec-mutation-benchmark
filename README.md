# FastAPI AppSec mutation benchmark

An independent static review identified **5 of 5 intentionally introduced defects** in a local FastAPI template. The benchmark measures how well the review surfaced those known issues on one snapshot.

The reviewer inspected the code before seeing the answer key. Seven normal HTTP controls passed. Verification of the flagged behavior over HTTP did not finish.

## Evidence

- [Benchmark index](benchmark.json) · [Boundary matrix index](matrices/boundaries.json)
- [Frozen findings](evidence/blind-static.json) · [Comparison against the answer key](evidence/comparison.json)
- [Recorded HTTP controls](evidence/runtime-smoke.json) · [Runtime status](evidence/runtime-status.json)
- [Upstream license](evidence/UPSTREAM-LICENSE.txt)

## Run the checks

[Open Case study checks in GitHub Actions](https://github.com/Keedz1Off/fastapi-appsec-mutation-benchmark/actions/workflows/checks.yml) and select **Run workflow**. CI runs two offline tests that reconcile the matrix, findings and saved HTTP controls.

The run saves `check-results`. Select **CD demo** to also package the passing log, commit SHA and checksum as `verified-delivery`.

Run locally with Python 3.10 or later:

```sh
python -B -m unittest discover -s tests -v
```

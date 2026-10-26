# Playwright E2E Testing Framework

A production-ready E2E testing setup using **pytest-playwright** with Page Object Model, parallel execution, and GitHub Actions CI/CD.

## Quick Start

```bash
# 1. Clone and enter project
cd e2e-playwright-project

# 2. Create virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt
playwright install

# 4. Run tests
pytest                    # All tests, headed, parallel
pytest -m smoke          # Smoke tests only
pytest --browser=firefox # Specific browser
pytest --headed --slowmo=1000 --pdb  # Debug mode
```

## Project Structure

```
e2e-playwright-project/
├── .github/workflows/ci.yml    # GitHub Actions CI/CD
├── pages/                      # Page Object Models
│   ├── __init__.py
│   └── login_page.py
├── tests/                      # Test files
│   ├── conftest.py             # Shared fixtures
│   └── test_login.py
├── pytest.ini                  # pytest configuration
├── requirements.txt            # Python dependencies
└── README.md
```

## Key Features

| Feature | Implementation |
|---------|----------------|
| **Page Object Model** | `pages/login_page.py` - maintainable, reusable |
| **Parallel Execution** | `pytest-xdist` with `-n auto` |
| **Multi-browser** | Chromium, Firefox, WebKit via matrix |
| **HTML Reports** | `pytest-html` with `--html=reports/report.html` |
| **JUnit XML** | CI dashboard integration |
| **Video Recording** | Auto-captured on failure |
| **Environment Config** | `BASE_URL` via GitHub Secrets |

## Running Tests

### Local Development
```bash
# All tests (headed, parallel, slowmo for visibility)
pytest

# Headless (faster, for CI)
pytest --headless

# Specific test file
pytest tests/test_login.py

# With markers
pytest -m smoke        # Quick smoke tests
pytest -m regression   # Full regression suite

# Debug mode - pauses on failure
pytest --headed --slowmo=1000 --pdb
```

### CI/CD (GitHub Actions)
The workflow runs on:
- Push to `main`/`develop`
- Pull requests to `main`
- Nightly schedule (2 AM UTC)

**Matrix**: Python 3.11, 3.12 × Chromium, Firefox, WebKit

**Artifacts uploaded**:
- HTML reports (always)
- Videos (on failure only)
- JUnit XML (for CI dashboards)

## Configuration

### Environment Variables
Set in GitHub Secrets or local `.env`:
```bash
BASE_URL=https://your-staging-app.com
```

### pytest.ini Options
```ini
addopts = 
    --headed              # Show browser (remove for CI)
    --slowmo=100          # Slow down actions (ms)
    --browser=chromium    # Default browser
    --html=reports/report.html
    --self-contained-html # Single-file report
    -n auto               # Auto parallel workers
```

## Adding New Tests

1. **Create Page Object** in `pages/`:
```python
# pages/checkout_page.py
class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        # ... locators
```

2. **Export in `pages/__init__.py`**:
```python
from pages.checkout_page import CheckoutPage
__all__ = ["LoginPage", "CheckoutPage"]
```

3. **Write test** in `tests/`:
```python
# tests/test_checkout.py
from pages.checkout_page import CheckoutPage

def test_checkout(page, base_url):
    CheckoutPage(page).goto().complete_purchase()
```

## Debugging Tips

- **Trace Viewer**: Add `--trace=on` to generate `.zip` traces
- **Screenshots**: `page.screenshot(path="debug.png")` in tests
- **Console Logs**: `page.on("console", print)` in fixtures
- **Pause**: `page.pause()` opens Playwright Inspector

## Requirements

- Python 3.11+
- Node.js (for Playwright browsers)
- GitHub Actions (for CI/CD)

## License

MIT
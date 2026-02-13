# Tech Stack Survey - Discussion Post Response

## Stack 1: Python / Django

**Backend language:** Python

**Framework:** Django 4.2

**Templating/rendering:** Django Templates

**UX/UI:** Bootstrap 5

**Testing:** pytest with pytest-django

**Debugging:** Django Debug Toolbar, Python debugger (pdb), VS Code Python extension

**Pros/cons:**
- ✅ **Excellent documentation & community:** Django has one of the best documentation sets in web development with extensive community support. Large ecosystem of third-party packages.
- ❌ **Performance overhead:** Django is an opinionated, batteries-included framework which can add overhead for simple applications compared to lighter frameworks.
- ✅ **Rapid development:** Convention-over-configuration approach enables fast development. Built-in ORM, admin panel, authentication, and database migration tools.

---

## Stack 2: C# / ASP.NET Core

**Backend language:** C#

**Framework:** ASP.NET Core 8.0 MVC

**Templating/rendering:** Razor Views

**UX/UI:** Bootstrap 5

**Testing:** xUnit or NUnit with xunit.analyzers

**Debugging:** Visual Studio or VS Code C# extension debugger, structured logging

**Pros/cons:**
- ✅ **High performance:** Compiled language with excellent async/await support, one of the fastest web frameworks available for throughput and response times.
- ❌ **Steeper learning curve:** More verbose syntax, requires understanding of C# generics and dependency injection patterns. Larger codebase compared to scripting languages.
- ✅ **Strong enterprise backing:** Microsoft actively maintains and invests in ASP.NET Core. Excellent tooling with Visual Studio and mature ecosystem.

---

## Stack 3: Ruby / Rails

**Backend language:** Ruby

**Framework:** Ruby on Rails 7.0

**Templating/rendering:** ERB (Embedded Ruby)

**UX/UI:** Bootstrap 5 or Tailwind CSS

**Testing:** RSpec with Rails test helpers

**Debugging:** byebug, rails logs, Rails server debug output

**Pros/cons:**
- ✅ **Fastest prototyping:** "Convention over configuration" philosophy enables building features extremely rapidly. Elegant, readable syntax that's easy to learn.
- ❌ **Runtime interpretation:** Ruby is interpreted, not compiled, resulting in slower startup times and runtime performance compared to compiled languages.
- ✅ **Mature ecosystem:** Rails has been around since 2004 with proven patterns for scalability. Great for startups and MVPs (Minimum Viable Products).

---

## Chosen Stack to do Hello World: **Python / Django**

**Reason:** I chose Django because it provides the best balance of ease-of-use, comprehensive documentation, and built-in features for learning. Django's templating system is intuitive and clearly demonstrates server-side rendering, which is essential for understanding the assignment requirements. The framework includes batteries-in-the-box (ORM, admin, migrations, testing), making it perfect for a Hello World demo while still being professional-grade. Python's readable syntax makes debugging straightforward and visible. Finally, Django runs well on EC2 with Linux and has proven production deployments, meeting the course requirements.

---

## Hello World Evidence

### Route/Controller

**File:** `hello/views.py`
```python
from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    """
    View function that renders the Hello World page.
    Demonstrates a simple request/response cycle that can be debugged.
    """
    context = {
        'message': 'Hello World!',
        'title': 'Hello World App',
    }
    return render(request, 'hello/index.html', context)
```

**URL Configuration:** `hello/urls.py`
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_world, name='hello_world'),
]
```

### Template/View

**File:** `hello/templates/hello/index.html`
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <!-- Bootstrap 5 CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        .container-center {
            text-align: center;
            background: white;
            padding: 60px;
            border-radius: 10px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.2);
        }
    </style>
</head>
<body>
    <div class="container-center">
        <h1>{{ message }}</h1>
        <p class="lead">Welcome to the Django Hello World App</p>
        <span class="badge bg-success">Using Django Templates with Bootstrap 5</span>
    </div>
</body>
</html>
```

**Note:** This demonstrates Django Templates with `{{ variable }}` syntax passing context from the view to the template. The template is rendered server-side before being sent to the client.

### UI Framework Proof

The template uses **Bootstrap 5** CDN for styling:
- Bootstrap CSS loaded from CDN: `https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css`
- Bootstrap utility classes used: `.badge`, `.bg-success`, responsive design with Flexbox
- Custom CSS styling with gradient backgrounds and card-like layout

### Test + Results

**Test File:** `hello/tests.py`

Automated test suite with 5 tests using pytest-django:

```
============== test session starts ==============
platform linux -- Python 3.12.12, pytest-9.0.2
collected 5 items

hello/tests.py::TestHelloWorldView::test_hello_world_view_returns_200 PASSED [ 20%]
hello/tests.py::TestHelloWorldView::test_hello_world_view_contains_message PASSED [ 40%]
hello/tests.py::TestHelloWorldView::test_hello_world_view_uses_correct_template PASSED [ 60%]
hello/tests.py::TestHelloWorldView::test_hello_world_view_contains_bootstrap PASSED [ 80%]
hello/tests.py::TestHelloWorldView::test_context_contains_message PASSED [100%]

============== 5 passed in 0.56s ==============
```

**Tests validate:**
1. HTTP 200 response code
2. "Hello World!" message in response
3. Correct template is used (hello/index.html)
4. Bootstrap CSS is included in the rendered HTML
5. Context variables are properly passed to the template

### Debugging Approach

Django provides multiple debugging tools:

1. **Django Debug Toolbar:** Interactive HTML panel showing SQL queries, request/response details, template rendering time
2. **Python pdb debugger:** Can add `import pdb; pdb.set_trace()` in views.py to step through code execution
3. **Server logs:** Django development server shows all HTTP requests, template rendering, and errors
4. **VS Code Python Debugger:** Full breakpoint and stepping support with Python extension

**Example debugging in the view:**
```python
def hello_world(request):
    # Add breakpoint to inspect request object
    import pdb; pdb.set_trace()
    context = {
        'message': 'Hello World!',
        'title': 'Hello World App',
    }
    return render(request, 'hello/index.html', context)
```

### Screenshots/Repo Information

**Running Application:**
- Server: `Django version 4.2, using settings 'helloworld.settings'`
- URL: `http://localhost:8001/` (mapped from Docker container port 8000)
- Status: "Watching for file changes with StatReloader" - Django auto-reloads on code changes

**Project Structure:**
```
django-helloworld/
├── manage.py                           # Django management script
├── requirements.txt                    # Python dependencies
├── pytest.ini                          # Pytest configuration
├── helloworld/                         # Project settings
│   ├── settings.py                     # Django settings
│   ├── urls.py                         # URL routing
│   └── wsgi.py                         # WSGI application
└── hello/                              # Django app
    ├── views.py                        # View logic
    ├── urls.py                         # App URL patterns
    ├── tests.py                        # Pytest test suite (5 tests)
    ├── models.py                       # Database models (empty for Hello World)
    └── templates/
        └── hello/
            └── index.html              # HTML template with Bootstrap
```

**Repository:** This implementation is contained in `django-helloworld/` directory and demonstrates all requirements:
- ✅ Server runs locally (Django development server on port 8001)
- ✅ One route (`/`) that renders "Hello World"
- ✅ Uses Django Templates for server-side rendering
- ✅ Uses Bootstrap 5 for styling and UI
- ✅ Includes 5 automated tests (all passing)
- ✅ Demonstrates debugging capabilities (pdb, Django logs, server output)

---

## Submission Details

This response includes:
1. ✅ Research on 3 meaningfully different tech stacks (Python/Django, C#/ASP.NET Core, Ruby/Rails)
2. ✅ Complete comparison across all 6 required criteria
3. ✅ Implemented "Hello World" app with all required features
4. ✅ Working automated test suite with passing tests
5. ✅ Evidence of debugging capabilities
6. ✅ Proper formatting following the discussion post structure

The Django Hello World application successfully demonstrates a modern, professional web framework with all components working together.

# Setting up a new Python project

This how-to uses the native ***venv***. Goodbye to pipenv. **[pyenv](https://github.com/pyenv/pyenv)** still used.  Tested as my current workflow on Mac OS.  Linux should be happy, too.
---

## A. Detailed steps
1. Choose your Python version
  * From available local versions - 
  ```bash
  ~/dev $ pyenv versions
  ```

  * Or from the Internet, if no local version exists -
  ```bash
  ~/dev $ pyenv install -l
  ~/dev $ pyenv install 3.7.4
  ```
2. Set the version as system default
```bash
~/dev $ pyenv global 3.7.4
```

3. Set up the project folder
```bash
~/dev $ mkdir project-x
~/dev $ cd project-x
~/dev/project-x $ mkdir venv
```

4. Create the virtual environment
```bash
~/dev/project-x $ python -m venv venv
```

5. Revert the system default Python version, if needed
```bash
~/dev/project-x $ pyenv global 3.6.8
```

6. Activate the virtual environment
```bash
~/dev/project-x $ source venv/bin/activate
```

7. Upgrade pip, if needed
```bash
(venv) ~/dev/project-x $ pip list
(venv) ~/dev/project-x $ pip install --upgrade pip
```

8. Work on the other Python packages, start-up VS Code, etc.

9. On VS Code, create a helloworld Python file to trigger VS Code asking for a Python interpreter; choose the appropriate venv and Python version. I also install pylint and black (via call to Format Document).  Sample pip list output of the base install -

```bash
(venv) ~/dev/project-x $ pip list
Package           Version
----------------- -------
appdirs           1.4.3
astroid           2.2.5
attrs             19.1.0
black             19.3b0
Click             7.0
isort             4.3.21
lazy-object-proxy 1.4.2
mccabe            0.6.1
pip               19.2.3
pylint            2.3.1
setuptools        40.6.2
six               1.12.0
toml              0.10.0
typed-ast         1.4.0
wrapt             1.11.2
(venv) ~/dev/project-x $
```

10. Before closing a working day's session, deactivate the virtual
```bash
(venv) ~/dev/project-x $ deactivate
~/dev/project-x $
```
---
## B. To recap
* to activate
```bash
~/dev/project-x $ source venv/bin/activate
```

* to deactivate
```bash
(venv) ~/dev/project-x $ deactivate
```

---
## C. Transitioning from a pyenv virtualenv to the native venv

Be sure to pip freeze > requirements first.

```bash
pyenv uninstall <name of pyenv virtual env>
```

Proceed to create the venv virtualenv.

Restore Python package dependencies

```bash
pip install -r requirements.txt
```

---
## D. Transitioning from a pipenv virtualenv to the native venv

Create a requirements from the pipenv lock output (copy-paste the output to requirements.txt) and remove the vm

```bash
pipenv lock -r
pipenv uninstall
pipenv --rm
```

Proceed to create the venv virtualenv.

Restore Python package dependencies

```bash
pip install -r requirements.txt
```

## E. Updating pyenv

In Homebrew:

```bash
$ brew update && brew upgrade pyenv
```

Update pyenv:

```bash
$ pyenv update
```
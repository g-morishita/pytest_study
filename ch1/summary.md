# How to use Pytest
## Install
Just `pip install -U pytest`.

Check if pytest is installed correctly by typing the following command.
`pytest --version`

If you see the following message, it is correctly installed.
```
This is pytest version 4.0.2, imported from /Users/s05905/anaconda3/lib/python3.7/site-packages/pytest.py
setuptools registered plugins:
  xonsh-0.9.5 at /Users/s05905/anaconda3/lib/python3.7/site-packages/xonsh/pytest_plugin.py
    pytest-remotedata-0.3.1 at /Users/s05905/anaconda3/lib/python3.7/site-packages/pytest_remotedata/plugin.py
      pytest-openfiles-0.3.1 at /Users/s05905/anaconda3/lib/python3.7/site-packages/pytest_openfiles/plugin.py
        pytest-doctestplus-0.2.0 at /Users/s05905/anaconda3/lib/python3.7/site-packages/pytest_doctestplus/plugin.py
          pytest-arraydiff-0.3 at /Users/s05905/anaconda3/lib/python3.7/site-packages/pytest_arraydiff/plugin.py
```

## Test
`pytest` tests python scripts whose name start with `test_` or end with `_test`.

Next, inside these scripts, it looks for functions which starts with `test_` and classes which starts with `Test` to test them.

You can test specific files by specifying files. For example, `pytest test_one.py test_two.py`.

Moreover, you can test specific functions or classes in a python script by using `::`. For instance, `pytest test_three.py::test_defaults`.

## Useful Options

### `--collect-only`
`pytest --collect-only`

It shows you which tests will be run. It's like dry-run, I guess.

### `-k EXPRESSION`
By using `-k` option, you can tell pytest what functions to be test.

For example, `-k "asdict or defautlts"`

### `-x`
This option tells pytest that if one test fails even though there are functions to be test afterward, stop the entire test.

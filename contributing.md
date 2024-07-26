<!-- Copyright 2024 PYBROTOOLS authors. -->
<!-- See license.md file for details. -->

# Contributing

This is the guide for contributing code, documentation and tests, and for
filing issues. Please read it carefully to help make the code review process go
as smoothly as possible and maximize the likelihood of your contribution being
merged.

<!-- @import "[TOC]" {cmd="toc" depthFrom=2 depthTo=3 orderedList=false} -->

<!-- code_chunk_output -->

- [How to contribute](#how-to-contribute)
- [Pull Request Checklist](#pull-request-checklist)
- [Filing bugs](#filing-bugs)
- [Documentation](#documentation)

<!-- /code_chunk_output -->

## How to contribute

The preferred workflow for contributing to *pybrotools* is to clone the
[main repository](https://github.com/brobertpc120/pybrotools/git) on
GitHub, and develop on a new branch. Steps:

1. Clone the *pybrotools* repository from your GitHub to your local disk.

2. Create a `feature` branch to hold your development changes.
    Always use a `feature` branch. It's good practice to never work on the
    `prod` branch!

3. Develop the feature on your feature branch. Add changed files using
    `git add` and then `git commit` files.

4. Add a meaningful commit message. Check out the
5. [seven commonly accepted rules](https://www.theserverside.com/video/Follow-these-git-commit-message-guidelines)
    for commit messages. Here are some examples, taken from actual commits:

   ```text
   Add support for new VRs OV, SV, UV

   -  closes #1016
   ```

   ```text
   Add warning when saving compressed without encapsulation
   ```

   ```text
   Add optional handler argument to Dataset.decompress()

   - also add it to Dataset.convert_pixel_data()
   - add separate error handling for given handle
   - see #537
   ```

6. To record your changes in Git, push the changes to your GitHub
    account with.

(If any of the above seems like magic to you, please look up the
[Git documentation](https://git-scm.com/documentation) on the web, or ask a
friend or another contributor for help.)

## Pull Request Checklist

We recommend that your contribution complies with the following rules before
you submit a pull request:

- Follow the style used in the rest of the code. That mostly means to follow
    [PEP-8 guidelines](https://www.python.org/dev/peps/pep-0008/) for the code,
    and the
    [Google style](https://github.com/google/styleguide/blob/gh-pages/pyguide.d#38-comments-and-docstrings)
    for documentation.

- If your pull request addresses an issue, please use the pull request title to
  describe the issue and mention the issue number in the pull request
  description. This will make sure a link back to the original issue is
  created. Use "closes #issue-number" or "fixes #issue-number" to let GitHub
  automatically close the related issue on commit. Use any other keyword
  (i.e. works on, related) to avoid GitHub to close the referenced issue.

- All public methods should have informative docstrings with sample usage
  presented as doctests when appropriate.

- Please prefix the name of a branch with `mrg` (Ready for Merge), if the
  contribution is complete and ready for a detailed review. Some of the core
  developers will review your code, make suggestions for changes, and merge it
  as soon as it is ready for merge. Branches are usually merged after one
  approval by one core developer, or other developers asked to review the code.
  An incomplete contribution -- where you expect to do more work before
  receiving a full review -- should be prefixed with `wip` (to indicate a work
  in progress) and changed to `mrg` when it matures. WIPs may be useful to:
  indicate you are working on something to avoid duplicated work, request broad
  review of functionality or API, or seek collaborators. WIPs often benefit
  from the inclusion of a
  [task list](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments)
  in the PR description.

- When adding additional functionality, check if it makes sense to add one or
  more example scripts in the `examples/` folder. Have a look at other examples
  for reference. Examples should demonstrate why the new functionality is
  useful in practice and, if possible, compare it to other methods available in
  *pybrotools*.

- Documentation and high-coverage tests are necessary for enhancements to be
  accepted. Bug-fixes shall be provided with
  [regression tests](https://en.wikipedia.org/wiki/regression_testing) that
  fail before the fix. For new features, the correct behavior shall be
  verified by feature tests. A good practice to write sufficient tests is
  [test-driven development](https://en.wikipedia.org/wiki/Test-driven_development).

You can also check for common programming errors and style issues with the
following tools:

- Code with good unittest **coverage** (current coverage or better), check with:

  ```bash
  make test
  ```

- No pyflakes warnings, no PEP8 warnings, check with:

  ```bash
  make format
  ```

## Filing bugs

We use GitHub issues to track all bugs and feature requests; feel free to
open an issue if you have found a bug or wish to see a feature implemented.

It is recommended to check that your issue complies with the
following rules before submitting:

- Verify that your issue is not being currently addressed by other
  [issues](https://github.com/brobertpc120/pybrotools/issues).

- Please ensure all code snippets and error messages are formatted in
  appropriate code blocks.
  See [Creating and highlighting code blocks](https://help.github.com/articles/creating-and-highlighting-code-blocks).

- Please include your operating system type and version number, as well
  as your Python and *pybrotools* versions.

- please include a
  [reproducible](https://stackoverflow.com/help/minimal-reproducible-example)
  code snippet or link to a [gist](https://gist.github.com). If an
  exception is raised, please provide the traceback. (use `%xmode`
  in ipython to use the non beautified version of the traceback)

## Documentation

We are glad to accept any sort of documentation: function docstrings,
reStructuredText documents, tutorials, etc. reStructuredText documents live in
the source code repository under the ``docs/`` directory.

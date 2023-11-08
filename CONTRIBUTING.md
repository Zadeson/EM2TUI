# Contributing to EM2 TUI

First off, thank you for considering contributing to EM2 TUI. It's people like you that make EM2 TUI such a great tool.

Following these guidelines helps to communicate that you respect the time of the developers managing and developing this open source project. In return, they should reciprocate that respect in addressing your issue, assessing changes, and helping you finalize your pull requests.

## Quick links

- [Code of Conduct](#code-of-conduct)
- [Getting Started](#getting-started)
- [What we are looking for](#what-we-are-looking-for)
- [How to report a bug](#how-to-report-a-bug)
- [How to suggest a feature or enhancement](#how-to-suggest-a-feature-or-enhancement)
- [How to submit changes](#how-to-submit-changes)
- [Style Guide / Coding conventions](#style-guide--coding-conventions)
- [Code Review Process](#code-review-process)

## Code of Conduct

This project and everyone participating in it is governed by the EM2 TUI Code of Conduct. By participating, you are expected to uphold this code. Please report unacceptable behavior to [your-email@domain.com].

## Getting Started

Before you submit your contribution, please make sure to take a moment and read through the following:

- Read the [README](README.md) for project background and setup instructions.
- Check the issues for open bugs and suggested enhancements to avoid duplicating efforts.

## What we are looking for

We love contributions from the community! Here are some ways you can help:

- Bug reports
- Bug fixes
- Performance improvements
- Feature implementations
- Improvements to documentation
- Test improvements

## How to report a bug

If you find a security vulnerability, do NOT open an issue. Email [your-email@domain.com] instead.

If you find a bug in the source code, a mistake in the documentation, or a flaw in the interface, you can help us by submitting an issue to our [GitHub Repository](https://github.com/yourusername/em2-tui). Even better you can submit a Pull Request with a fix.

**Please see the [Issues](https://github.com/yourusername/em2-tui/issues) page before you submit a bug to avoid duplicate reports.**

## How to suggest a feature or enhancement

If you find yourself wishing for a feature that doesn't exist in EM2 TUI, you are probably not alone. There are bound to be others out there with similar needs. Open an issue on our [issues list](https://github.com/yourusername/em2-tui/issues) on GitHub which describes the feature you would like to see, why you need it, and how it should work.

## How to submit changes

After getting some feedback, you can make changes to your fork and submit a pull request:

1. Fork the repository.
2. Make your changes in a new git branch:

```
git checkout -b my-fix-branch master
```

3. Create your patch, **including appropriate test cases**.
4. Commit your changes using a descriptive commit message.

```
git commit -am "Add a brief description of the fix"
```

5. Push your branch to GitHub:

```
git push origin my-fix-branch
```

6. In GitHub, send a pull request to `em2-tui:master`.

### After your pull request is merged

After your pull request is merged, you can safely delete your branch and pull the changes from the main (upstream) repository:

- Delete the remote branch on GitHub either through the GitHub web UI or your local shell as follows:

```
git push origin --delete my-fix-branch
```

- Check out the master branch:

```
git checkout master -f
```

- Delete the local branch:

```
git branch -D my-fix-branch
```

- Update your master with the latest upstream version:

```
git pull --ff upstream master
```

## Style Guide / Coding conventions

- We follow PEP 8 for Python code style.
- Include comments in your code where necessary.
- Write detailed descriptions in your commit messages.
- Write tests where possible.

## Code Review Process

The core team looks at Pull Requests on a regular basis. After feedback has been given we expect responses within two weeks. After two weeks we may close the pull request if it isn't showing any activity.

Remember that contributions to this repository are considered to be under the same [license](LICENSE.md) as the repository.

## Thank you for your contributions!

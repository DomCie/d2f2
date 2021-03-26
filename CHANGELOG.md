# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

* More output formats (EPUB, MOBI)
* Custom order for images
* Modify names of output files
* Standalone GUI client

## [2.0.2] - 2021-03-26

### Removed

* Required Python version is no longer limited to versions higher than 3.9

## [2.0.1] - 2021-03-08

### Fixed

* A critical bug regarding conversion routines 
* Formatting of help messages

## [2.0.0] - 2021-03-08

### Added

* CBZ support
* Tool can now be directly accessed from the command line without using ``python -m``

### Changed

* Changed module name from DIRtoPDF to D2F2
* Code revamp

## [1.2.1] - 2021-03-04

### Fixed

* Fixed display of help messages
* Updated documentation

## [1.2.0] - 2021-03-02

### Added

* Sorting modes: specify how your images will be sorted inside the PDF file
* Standalone shell clients for Windows and Linux (see [Releases](https://github.com/DomCie/DIRtoPDF/releases))

### Fixed

* Names of PDF files can be empty when path ends with a slash or backslash

## [1.1.0] - 2021-02-25

### Added

* Interactive shell (without own client)

### Changed

* Code improvements

### Fixed

* Generated PDF's names don't match with the actual basename of their source directory

## [1.0.1] - 2021-02-22

### Changed

* Code improvements
* Updated README

## [1.0.0] - 2021-02-22

### Added

* Core functionality: convert image folders into PDF files over CLI
* "Multiple" mode for converting batches of folders more easily

[Unreleased]: https://github.com/DomCie/D2F2/compare/v2.0.2...HEAD
[2.0.2]: https://github.com/DomCie/D2F2/compare/v2.0.1...v2.0.2
[2.0.1]: https://github.com/DomCie/D2F2/compare/v2.0.0...v2.0.1
[2.0.0]: https://github.com/DomCie/D2F2/compare/v1.2.1...v2.0.0
[1.2.1]: https://github.com/DomCie/D2F2/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/DomCie/D2F2/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/DomCie/D2F2/compare/v1.0.1...v1.1.0
[1.0.1]: https://github.com/DomCie/D2F2/compare/v1.0.0...v1.0.1
[1.0.0]: https://github.com/DomCie/D2F2/releases/tag/v1.0.0
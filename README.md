# Oreo Nord Cursors

This is my fork of [varlesh/oreo-cursors](https://github.com/varlesh/oreo-cursors), with [Nord](https://nordtheme.com) colours.

### Arch (AUR)
```console
paru -S oreo-nord-cursors-git
```

### Manual Install
1. Install dependencies:
    - git
    - make
    - inkscape
    - xcursorgen

2. Run the following commands as normal user:
```console
git clone https://github.com/0jdxt/oreo-nord-cursors.git
cd oreo-nord-cursors
make build
sudo make install
```

3. Choose a theme in the Settings or in the Tweaks tool.


### Changes:
Removed original colours and refactored to use a base directory, allowing any colour of cursor to be generated by the `generate.sh` script.
This repo has been packaged for the AUR.


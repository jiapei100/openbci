# OpenBCI framework

OpenBCI is a platform for Brain Computer Interfaces. This software contains tools which allow you to build a complete Brain Computer Interface based on EEG, and perform some experiments collecting EEG and other biomedical data signals.

These tools are:

 * tools for communication with some EEG hardware (TMSi, Braintronics, and openEEG)
 * tools for displaying and storing the EEG (and other biomedical time series) signal
 * tools for creating "bindings" or "use scenarios" for some 3rd party software for performing psychological experiments (e-prime, psychopy, visionEGG). This means, that if you prepare an experiment in some of mentioned software, you will be able to perform this experiment, and store the EEG data, with necessary tags using OpenBCI.

# Installing

### From packages

On certain Ubuntu versions OpenBCI can be installed from packages available at http://deb.braintech.pl.

### From git

Download OpenBCI source code:

```
$ cd ~
$ git clone https://github.com/BrainTech/openbci.git
```

Now run script to configure OpenBCI locally. When asked, answer 'y' to install binaries inside <code>~/bin</code> directory:

```
$ cd ~/openbci/scripts
$ ./obci_local activate ../../openbci
```

Running OpenBCI from source requires globally installed Azuk-Multiplexer and may require amplifier drivers. It's highly recommended to install this software from precompiled packages available at http://deb.braintech.pl.

# Usage

Following programs are available from command line:
 * <code>obci</code> - main OpenBCI script
 * <code>obci_gui</code> - OpenBCI scenario selector GUI
 * <code>obci_tray</code> - tray application
 * <code>obci_local</code> - script for configuring local copy of OpenBCI (can be used to configure OpenBCI when openbci-core package is not installed)

# License

OpenBCI is licensed under the terms of the GNU GPL version 3.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.


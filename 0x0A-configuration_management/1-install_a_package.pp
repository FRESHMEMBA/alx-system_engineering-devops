#!/usr/bin/pup
# Installs a package

package {'python3-flask':
    ensure   => '2.1.0',
    provider => 'pip3'
}
# Installs a package

package {'python3-flask':
    ensure   => 'installed',
    provider => 'pip'
}
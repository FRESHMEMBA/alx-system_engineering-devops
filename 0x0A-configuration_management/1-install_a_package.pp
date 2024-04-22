# Installs a package

package {'flask':
    ensure   => 'installed',
    provider => 'pip'
}
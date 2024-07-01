# Installs a package

# Ensure that python3 is installed
package {'python3':
    ensure => installed,
}

# Ensure that pip3 is installed
pacakge {'python3-pip':
    ensure => installed,
}

# Ensure Flask v2.1.0 is installed using pip3
package {'Flask':
    ensure   => '2.1.0',
    provider => 'pip3',
    require  => package['python3-pip'],
}
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
exec {'Install_flask':
    command  => '/usr/bin/pip3 install flask==2.1.0',
    unless   => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
    require  => package['python3', 'python3-pip'],
}
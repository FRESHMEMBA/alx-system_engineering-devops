# This manifest increases the number of open file descriptors for the 'holberton' user

# Ensure the limits are set for the holberton user
exec { 'change-os-configuration-for-holberton-user':
    command => 'echo "holberton soft nofile 65535" >> /etc/security/limits.conf ' +
               '&& echo "holberton hard nofile 65535" >> /etc/security/limits.conf',
    unless  => 'grep -q "holberton.*nofile" /etc/security/limits.conf',
}

# Restart the session or apply the changes to take effect
exec { 'apply-limits':
    command => '/bin/su -c "ulimit -n 65535" holberton',
    require => Exec['change-os-configuration-for-holberton-user'],
}

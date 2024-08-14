# Puppet Manifest: 0-strace_is_your_friend.pp

# Ensure the correct file reference in wp-settings.php
exec { 'fix-wp-locale-typo':
    command => 'sed -i "s/class-wp-locale.phpp/class-wp-locale.php/" /var/www/html/wp-settings.php',
    onlyif  => 'grep "class-wp-locale.phpp" /var/www/html/wp-settings.php',}

# Restart Apache to apply the changes
service { 'apache2':
    ensure  => running,
    enable  => true,
    require => File_line['fix-wp-locale-typo'],
}

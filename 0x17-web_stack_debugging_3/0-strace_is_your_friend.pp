# Puppet Manifest: 0-strace_is_your_friend.pp

# Ensure the correct file reference in wp-settings.php
file_line { 'fix-wp-locale-typo':
    path  => '/var/www/html/wp-settings.php',
    match => 'class-wp-locale.phpp',
    line  => 'require_once(ABSPATH . WPINC . "/class-wp-locale.php);',
}

# Restart Apache to apply the changes
service { 'apache2':
    ensure  => running,
    enable  => true,
    require => File_line['fix-wp-locale-typo'],
}

# Optimizes Nginx configuration to handle high traffic loads without failing.

exec { 'optimize-nginx':
    command => '/usr/sbin/nginx -s reload',
    onlyif  => 'test -f /etc/nginx/nginx.conf',
}

# Ensure the worker processes and connections are set to handle high load
file { '/etc/nginx/nginx.conf':
    ensure  => file,
    content => template('nginx/nginx.conf.erb'),
    notify  => Exec['optimize-nginx'],
}

# Create the optimized Nginx configuration file using an ERB template
file { '/etc/nginx/nginx.conf.erb':
    ensure  => file,
    content => @("CONFIG")
    user nginx;
    worker_processes auto;

    events {
        worker_connections 1024;
    }

    http {
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        gzip on;
        gzip_disable "msie6";

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
    }
    | CONFIG
}

# Restart the Nginc service to apply changes
service { 'nginx':
    ensure  => running,
    enable  => true,
    require => File['/etc/nginx/nginx.conf'],
}
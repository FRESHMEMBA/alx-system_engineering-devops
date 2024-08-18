### Postmortem: Apache 500 Error Due to Typo in WordPress Configuration

**Incident Date**: August 14, 2024  
**Author**: Sibonelo Mazibuko

---

#### **Summary**

On August 14, 2024, a critical error occurred on a web server running Apache, which led to a 500 Internal Server Error. The issue was traced to a typo in the WordPress configuration file (`wp-settings.php`). The typo involved an incorrect reference to a PHP file, specifically `class-wp-locale.phpp` instead of `class-wp-locale.php`. This caused Apache to fail in processing requests, resulting in the server returning a 500 error. The issue was resolved by identifying the typo using `strace` and then automating the fix with a Puppet script.

#### **Timeline**

- **12:47 PM**: Apache server starts, but immediately begins returning 500 errors on all incoming requests.
- **12:51 PM**: Initial diagnostics with `ps aux | grep apache2` confirm Apache is running, but the 500 error persists.
- **12:53 PM**: `strace` is used to trace the system calls of the Apache process. The trace reveals that Apache is attempting to access a non-existent file `class-wp-locale.phpp`.
- **12:54 PM**: Further investigation using `grep` confirms that the typo is present in the `wp-settings.php` file.
- **1:00 PM**: A Puppet manifest (`temp.pp`) is created to automatically correct the typo in the configuration file.
- **1:05 PM**: The Puppet manifest is successfully applied, fixing the typo and restarting Apache. The server begins responding with HTTP 200 OK status.

#### **Root Cause**

The root cause of the incident was a typo in the `wp-settings.php` file, where `class-wp-locale.phpp` was mistakenly written instead of `class-wp-locale.php`. This typo caused Apache to fail when attempting to include the PHP file, resulting in a 500 Internal Server Error.

#### **Resolution**

1. **Issue Identification**: Used `strace` to identify that Apache was failing to locate the `class-wp-locale.phpp` file.
   
2. **Verification**: Used `grep` to confirm the presence of the typo in the `wp-settings.php` file.

3. **Automated Fix**: Created a Puppet manifest (`temp.pp`) to:
   - Correct the typo by replacing `class-wp-locale.phpp` with `class-wp-locale.php`.
   - Restart the Apache service to apply the fix.

4. **Verification of Fix**: Verified that Apache returned HTTP 200 OK status after applying the fix.

#### **Lessons Learned**

- **Importance of Automation**: The use of Puppet to automate the fix not only resolved the issue but also provided a template for handling similar issues in the future.
- **Thorough Testing**: Before deployment, configuration files should be thoroughly tested to avoid simple yet impactful errors like typos.
- **Monitoring and Tracing**: Tools like `strace` are invaluable for quickly diagnosing issues at the system call level, which can be critical in resolving complex errors.

#### **Preventative Measures**

- **Code Review**: Implement stricter code review processes, especially for configuration files, to catch typos and other minor errors before they reach production.
- **Automated Testing**: Introduce automated testing for configuration files to ensure that all required files are correctly referenced.
- **Regular Audits**: Conduct regular audits of server configuration and deployment scripts to ensure they adhere to best practices.

---

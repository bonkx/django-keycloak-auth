from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from login_required import login_not_required

# Create your views here.


@login_not_required
def public(request):
    return render(request, "web/public.html", {})


# @login_required
def index(request):
    # user = request.user
    # if request.user.is_authenticated:
    #     oidc_access_token = request.session['oidc_access_token']
    #     print("oidc_access_token : ", oidc_access_token)
    #     oidc_id_token = request.session['oidc_id_token']
    #     print("oidc_id_token : ", oidc_id_token)
    # print(settings.KC_BASE_URI)
    host = "%s://%s" % (
        request.META['wsgi.url_scheme'],
        request.META['HTTP_HOST'],
    )
    print(host)

    # {'SHELL': '/bin/bash', 'COLORTERM': 'truecolor', 'XPC_FLAGS': '0x0', 'TERM_PROGRAM_VERSION': '1.85.1', 'GIT_PS1_SHOWUPSTREAM': 'auto',
    # '__CFBundleIdentifier': 'com.microsoft.VSCode', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.gJ0aZwSpWa/Listeners',
    # 'MallocNanoZone': '0', 'GIT_PS1_SHOWDIRTYSTATE': '1', 'ANDROID_SDK': '/Users/bonk/Library/Android/sdk',
    # 'PWD': '/Users/bonk/webapp/@Nawastra/keycloak-frontend/apepe-django-keycloak-auth/dash', 'LOGNAME': 'macbook',
    # 'VSCODE_GIT_ASKPASS_NODE': '/Applications/Visual Studio Code.app/Contents/Frameworks/Code Helper (Plugin).app/Contents/MacOS/Code Helper (Plugin)',
    # 'COMMAND_MODE': 'unix2003', 'HOME': '/Users/bonk', 'LANG': 'en_US.UTF-8',
    # 'VIRTUAL_ENV': '/Users/bonk/webapp/@Nawastra/keycloak-frontend/apepe-django-keycloak-auth/venv',
    # 'TMPDIR': '/var/folders/gq/b8yb54wx5fx9d5w9pjzlg1b00000gn/T/',
    # 'GIT_ASKPASS': '/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass.sh',
    # 'GOROOT': '/usr/local/opt/go/libexec', 'VSCODE_GIT_ASKPASS_EXTRA_ARGS': '--ms-enable-electron-run-as-node', 'TERM': 'xterm-256color',
    # 'USER': 'macbook', 'VSCODE_GIT_IPC_HANDLE': '/var/folders/gq/b8yb54wx5fx9d5w9pjzlg1b00000gn/T/vscode-git-6ef1f47a2f.sock', 'SHLVL': '2',
    # 'VIRTUAL_ENV_PROMPT': '(venv) ', 'XPC_SERVICE_NAME': '0',
    # 'PS1': '\\[\x1b]633;A\x07\\](venv) \\[\x1b]633;A\x07\\]\\[\x1b]633;A\x07\\]\\[\\033[32m\\]\\u@\\h\\[\\033[00m\\]:\\W\\[\\033[31m\\]$(__git_ps1)\\[\\033[00m\\]\\$ \\[\x1b]633;B\x07\\]\\[\x1b]633;B\x07\\]\\[\x1b]633;B\x07\\]',
    # 'VSCODE_GIT_ASKPASS_MAIN': '/Applications/Visual Studio Code.app/Contents/Resources/app/extensions/git/dist/askpass-main.js',
    # 'PATH': '/Users/bonk/webapp/@Nawastra/keycloak-frontend/apepe-django-keycloak-auth/venv/bin:/usr/local/opt/python@3.8/bin:/Users/bonk/Library/Android/sdk/emulator:/Users/bonk/Library/Android/sdk/tools:/usr/local/sbin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/Users/bonk/Developer/flutter/bin:/Users/bonk/.composer/vendor/bin:/usr/sbin:/usr/local/mysql/bin/:/usr/local/opt/mysql-client/bin:/usr/local/Cellar/mysql@5.6/5.6.47/bin:/usr/local/bin/dart:/Users/bonk/Developer/flutter/.pub-cache/bin:/Users/bonk/.pub-cache/bin:/Users/bonk/go//bin:/usr/local/opt/go/libexec/bin',
    # 'ORIGINAL_XDG_CURRENT_DESKTOP': 'undefined', 'GOPATH': '/Users/bonk/go/', '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0', 'TERM_PROGRAM':
    # 'vscode', '_': '/Users/bonk/webapp/@Nawastra/keycloak-frontend/apepe-django-keycloak-auth/venv/bin/python3',
    # 'OLDPWD': '/Users/bonk/webapp/@Nawastra/keycloak-frontend/apepe-django-keycloak-auth',
    # 'DJANGO_SETTINGS_MODULE': 'dash.settings', 'KC_REALM': 'semarkepo', 'KC_CLIENT_ID': 'mozilla2', 'OIDC_RP_SCOPES': 'openid profile email',
    # 'KC_BASE_URI': 'https://auth.puskeu.polri.info', 'KC_CLIENT_SECRET': '5Mp7Z3g78ymIRLNu08CevcUakKl4hQAl',
    # 'LOGIN_REDIRECT_URL': 'http://localhost:8001', 'TZ': 'UTC', 'RUN_MAIN': 'true', 'SERVER_NAME': '1.0.0.127.in-addr.arpa',
    # 'GATEWAY_INTERFACE': 'CGI/1.1', 'SERVER_PORT': '8001', 'REMOTE_HOST': '', 'CONTENT_LENGTH': '', 'SCRIPT_NAME': '',
    # 'SERVER_PROTOCOL': 'HTTP/1.1', 'SERVER_SOFTWARE': 'WSGIServer/0.2', 'REQUEST_METHOD': 'GET', 'PATH_INFO': '/', 'QUERY_STRING': '',
    # 'REMOTE_ADDR': '127.0.0.1', 'CONTENT_TYPE': 'text/plain', 'HTTP_HOST': 'localhost:8001',
    # 'HTTP_CONNECTION': 'keep-alive', 'HTTP_PRAGMA': 'no-cache',
    # 'HTTP_CACHE_CONTROL': 'no-cache', 'HTTP_SEC_CH_UA': '"Not_A Brand";v="8", "Chromium";v="120",
    # "Google Chrome";v="120"', 'HTTP_SEC_CH_UA_MOBILE': '?0', 'HTTP_SEC_CH_UA_PLATFORM': '"macOS"',
    # 'HTTP_UPGRADE_INSECURE_REQUESTS': '1', 'HTTP_USER_AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    # 'HTTP_ACCEPT': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'HTTP_SEC_FETCH_SITE': 'none', 'HTTP_SEC_FETCH_MODE': 'navigate', 'HTTP_SEC_FETCH_USER': '?1', 'HTTP_SEC_FETCH_DEST': 'document',
    # 'HTTP_ACCEPT_ENCODING': 'gzip, deflate, br', 'HTTP_ACCEPT_LANGUAGE': 'en-US,en;q=0.9',
    # 'HTTP_COOKIE': 'csrftoken=qh7dvAPX8afNqkW9OUYdl426KAl7oKA6; sessionid=xquyxsr4kfbvlxjvsaokrksmfa3jl5bv', 'wsgi.input': <django.core.handlers.wsgi.LimitedStream object at 0x10d99f1c0>, 'wsgi.errors': <_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>,
    # 'wsgi.version': (1, 0), 'wsgi.run_once': False, 'wsgi.url_scheme': 'http', 'wsgi.multithread': True, 'wsgi.multiprocess': False,
    # 'wsgi.file_wrapper': <class 'wsgiref.util.FileWrapper'>, 'CSRF_COOKIE': 'qh7dvAPX8afNqkW9OUYdl426KAl7oKA6'}

    return render(request, "web/home.html", {})


# @login_required
def protected(request):
    return render(request, "web/protect.html", {})

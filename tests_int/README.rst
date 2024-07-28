How to run integration test in AWS EC2 where you run the worldserver:

SSH to the EC2 instance::

    sshec2 ssh

Delete existing code::

    rm -rf /home/ubuntu/git_repos/acore_soap-project

Git clone latest repo::

    git clone https://github.com/MacHu-GWU/acore_soap-project /home/ubuntu/git_repos/acore_soap-project

Git pull latest changes::

    cd /home/ubuntu/git_repos/acore_soap-project && git pull

CD to the repo dir::

    cd /home/ubuntu/git_repos/acore_soap-project

Create virtualenv::

    virtualenv /home/ubuntu/git_repos/acore_soap-project/.venv

Activate virutalenv::

    source /home/ubuntu/git_repos/acore_soap-project/.venv/bin/activate

Pip install core dependencies::

    /home/ubuntu/git_repos/acore_soap-project/.venv/bin/pip install -e /home/ubuntu/git_repos/acore_soap-project

Pip install test dependencies::

    /home/ubuntu/git_repos/acore_soap-project/.venv/bin/pip install -r /home/ubuntu/git_repos/acore_soap-project/requirements-test.txt

Run integration test::

    /home/ubuntu/git_repos/acore_soap-project/.venv/bin/pytest /home/ubuntu/git_repos/acore_soap-project/tests_int -s

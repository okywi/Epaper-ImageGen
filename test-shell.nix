{ pkgs ? import <nixpkgs> {} }:
(pkgs.buildFHSEnv {
  name = "test-pip-shell";
  targetPkgs = pkgs: (with pkgs; [
    python313
    python313Packages.pip
    python313Packages.virtualenv
  ]);
  profile = ''
  export PYTHONPATH=.
    if [ ! -d .venv ]; then
        python -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
    fi

    source .venv/bin/activate
  '';
  runScript = ''
    bash --init-file /etc/profile
  '';
}).env



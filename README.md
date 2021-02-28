# BC

Blockchain & Crypto

**ACTIVATE Virtual Env.**

```
source blockchain-env/bin/activate
```

**INSTALL all packages**

```
pip3 install -r requirements.txt
```

**RUN the tests**

Make sure to activate the V.ENV

```
python -m pytest backend/tests
```

**Run the app and API**

Make sure to activate the V.ENV

```
python3 -m backend.app
```

**Run a peer instance**

Make sure to activate the V.ENV

```
export PEER=True && python3 -m backend.app
```

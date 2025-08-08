source venv/bin/activate

python -m pytest tests/test_all.py --headless > /dev/null

PYTEST_EXIT_CODE=$?

if [ $PYTEST_EXIT_CODE -eq 0 ]
then
    exit 0
else
    exit 1
fi
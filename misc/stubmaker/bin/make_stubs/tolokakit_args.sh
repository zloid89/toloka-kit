cat << EOF
--module-root toloka \
--src-root $(dirname $0)/../../../../src/ \
--output-dir $(dirname $0)/../../../../src/
--described-objects $(dirname $0)/../../described_objects_tolokakit.py
EOF

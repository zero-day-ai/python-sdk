.PHONY: proto test lint fmt install clean

SDK_PROTO := ../sdk/api/proto
BUF_VALIDATE := $(HOME)/.cache/buf/v3/modules/b5/buf.build/bufbuild/protovalidate/50325440f8f24053b047484a6bf60b76/files

proto:
	uv run --with grpcio-tools python -m grpc_tools.protoc \
		-I $(SDK_PROTO) \
		-I $(BUF_VALIDATE) \
		--python_out=src \
		--grpc_python_out=src \
		--pyi_out=src \
		$(shell find $(SDK_PROTO) -name "*.proto" | grep -v "google/protobuf" | grep -v "options.proto" | grep -v "test/v1")

install:
	uv sync

test:
	uv run pytest -v

lint:
	uv run ruff check src tests

fmt:
	uv run ruff format src tests

clean:
	find src -name "*_pb2*.py" -o -name "*_pb2*.pyi" | xargs rm -f
	rm -rf dist __pycache__ .pytest_cache .ruff_cache

FROM ubuntu:22.04
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y curl git lz4 python3 python3-pip unzip
RUN curl -sL https://github.com/pygame-web/python-wasm-sdk/releases/download/3.1.46.bi/python3.11-wasm-sdk-Ubuntu-22.04.tar.lz4 -o sdk.tar.lz4 &&\
    tar xfP sdk.tar.lz4 --use-compress-program=lz4 &&\
    rm sdk.tar.lz4
RUN python3 -m pip install pygbag

COPY zengl-stubs /zengl/zengl-stubs
COPY setup.py MANIFEST.in README.md zengl.c _zengl.py _zengl_js.py /zengl/
RUN cd /zengl/ && /opt/python-wasm-sdk/python3-wasm setup.py bdist_wheel
RUN unzip /zengl/dist/zengl-2.2.0-cp311-cp311-wasm32_bi_emscripten.whl -d /web/

COPY examples/pygbag/public /web
CMD python3 -m pygbag --template noctx.tmpl /web/

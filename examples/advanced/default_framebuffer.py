import zengl

from window import Window

window = Window()
ctx = zengl.context()

pipeline = ctx.pipeline(
    vertex_shader='''
        #version 300 es
        precision highp float;

        out vec3 v_color;

        vec2 positions[3] = vec2[](
            vec2(0.0, 0.8),
            vec2(-0.6, -0.8),
            vec2(0.6, -0.8)
        );

        vec3 colors[3] = vec3[](
            vec3(1.0, 0.0, 0.0),
            vec3(0.0, 1.0, 0.0),
            vec3(0.0, 0.0, 1.0)
        );

        void main() {
            gl_Position = vec4(positions[gl_VertexID], 0.0, 1.0);
            v_color = colors[gl_VertexID];
        }
    ''',
    fragment_shader='''
        #version 300 es
        precision highp float;

        in vec3 v_color;

        layout (location = 0) out vec4 out_color;

        void main() {
            out_color = vec4(v_color, 1.0);
        }
    ''',
    framebuffer=None,
    viewport=(0, 0, window.size[0], window.size[1]),
    topology='triangles',
    vertex_count=3,
)

while window.update():
    ctx.new_frame()
    pipeline.render()
    ctx.end_frame()

import numpy as np
import zengl


def test_camera():
    camera = zengl.camera((4.0, 3.0, 2.0), (0.0, 0.0, 1.0))
    np.testing.assert_almost_equal(np.frombuffer(camera, 'f4'), [
        -1.039230465888977, -0.2717464864253998, -0.7846214771270752, -0.7844645380973816,
        1.3856406211853027, -0.20380987226963043, -0.5884661078453064, -0.588348388671875,
        0.0, 1.6984155178070068, -0.1961553692817688, -0.1961161345243454,
        0.0, -1.6984155178070068, 5.096174716949463, 5.295135498046875,
    ], 2)

    camera = zengl.camera(
        eye=(-6.2, 2.1, -3.3),
        target=(4.5, -9.7, 0.4),
        up=(0.3, -0.5, -0.6),
        fov=60.0,
        aspect=1.2,
        near=0.5,
        far=10.0,
    )

    np.testing.assert_almost_equal(np.frombuffer(camera, 'f4'), [
        1.090432047843933, 0.05827002227306366, 0.723190188407898, 0.6543149352073669,
        0.9194796085357666, -0.46960100531578064, -0.7975368499755859, -0.721580982208252,
        -0.2210170179605484, -1.6661571264266968, 0.250075101852417, 0.22625844180583954,
        4.100415229797363, -4.150882244110107, 5.931222915649414, 6.3187255859375,
    ], 2)

    camera = zengl.camera(
        eye=(-6.2, 2.1, -3.3),
        target=(4.5, -9.7, 0.4),
        up=(0.3, -0.5, -0.6),
        fov=60.0,
        aspect=1.2,
        near=0.5,
        far=10.0,
        clip=True,
    )

    np.testing.assert_almost_equal(np.frombuffer(camera, 'f4'), [
        1.090432047843933, 0.05827002227306366, 0.6887525916099548, 0.6543149352073669,
        0.9194796085357666, -0.46960100531578064, -0.759558916091919, -0.721580982208252,
        -0.2210170179605484, -1.6661571264266968, 0.23816677927970886, 0.22625844180583954,
        4.100415229797363, -4.150882244110107, 6.124974250793457, 6.3187255859375,
    ], 2)

    camera = zengl.camera(
        eye=(4.3, -7.6, 1.5),
        target=(-2.7, 7.4, 8.4),
        up=(-0.7, -0.7, 0.2),
        fov=0.0,
        aspect=1.33,
        near=2.0,
        far=50.0,
        size=5.0,
    )

    np.testing.assert_almost_equal(np.frombuffer(camera, 'f4'), [
        0.06684909760951996, -0.1612476259469986, -0.016263799741864204, 0.0,
        -0.029283832758665085, -0.10246407985687256, 0.03485099971294403, 0.0,
        0.1314784288406372, 0.059163451194763184, 0.016031460836529732, 0.0,
        -0.7072259187698364, -0.1741073876619339, -0.7725785970687866, 1.0,
    ], 2)

    camera = zengl.camera(
        eye=(4.3, -7.6, 1.5),
        target=(-2.7, 7.4, 8.4),
        up=(-0.7, -0.7, 0.2),
        fov=0.0,
        aspect=1.33,
        near=2.0,
        far=50.0,
        size=5.0,
        clip=True,
    )

    np.testing.assert_almost_equal(np.frombuffer(camera, 'f4'), [
        0.06684909760951996, -0.1612476259469986, -0.008131899870932102, 0.0,
        -0.029283832758665085, -0.10246407985687256, 0.017425499856472015, 0.0,
        0.1314784288406372, 0.059163451194763184, 0.008015730418264866, 0.0,
        -0.7072259187698364, -0.1741073876619339, 0.11371070891618729, 1.0,
    ], 2)

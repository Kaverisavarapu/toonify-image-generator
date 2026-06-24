from PIL import Image
import cv2
import numpy as np


def apply_realistic_oil_painting(img):
    import cv2, numpy as np
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (800, int(img.shape[0] * 800 / img.shape[1])))
    oil_base = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
    texture = cv2.edgePreservingFilter(img, flags=1, sigma_s=80, sigma_r=0.4)
    mixed = cv2.addWeighted(oil_base, 0.8, texture, 0.2, 0)
    lab = cv2.cvtColor(mixed, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)
    l = cv2.equalizeHist(l)
    enhanced = cv2.merge((l, a, b))
    final = cv2.cvtColor(enhanced, cv2.COLOR_LAB2BGR)
    final = cv2.convertScaleAbs(final, alpha=1.2, beta=25)
    hsv = cv2.cvtColor(final, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    s = np.clip(s * 1.15, 0, 255).astype(np.uint8)
    hsv_enhanced = cv2.merge([h, s, v])
    final = cv2.cvtColor(hsv_enhanced, cv2.COLOR_HSV2BGR)
    return cv2.cvtColor(final, cv2.COLOR_BGR2RGB)

def apply_realistic_pencil_sketch(img):
    import cv2, numpy as np
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (800, int(img.shape[0] * 800 / img.shape[1])))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    inv = 255 - gray
    blur = cv2.GaussianBlur(inv, (25, 25), 0)
    sketch = cv2.divide(gray, 255 - blur, scale=256)
    paper = np.random.normal(128, 30, sketch.shape).astype(np.uint8)
    blended = cv2.addWeighted(sketch, 0.9, paper, 0.1, 0)
    return cv2.cvtColor(blended, cv2.COLOR_GRAY2RGB)

def apply_vintage_effect(img):
    import cv2, numpy as np
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (800, int(img.shape[0] * 800 / img.shape[1])))
    sepia = np.array([[0.272, 0.534, 0.131],
                      [0.349, 0.686, 0.168],
                      [0.393, 0.769, 0.189]])
    vintage = cv2.transform(img, sepia)
    vintage = np.clip(vintage, 0, 255).astype(np.uint8)
    alpha, beta = 0.9, 15
    faded = cv2.convertScaleAbs(vintage, alpha=alpha, beta=beta)
    rows, cols = faded.shape[:2]
    kernel_x = cv2.getGaussianKernel(cols, 200)
    kernel_y = cv2.getGaussianKernel(rows, 200)
    kernel = kernel_y * kernel_x.T
    mask = kernel / kernel.max()
    vignette = np.copy(faded)
    for i in range(3):
        vignette[:, :, i] = vignette[:, :, i] * mask
    noise = np.random.normal(0, 10, vignette.shape).astype(np.uint8)
    grainy = cv2.addWeighted(vignette, 0.95, noise, 0.05, 0)
    return cv2.cvtColor(grainy, cv2.COLOR_BGR2RGB)

def apply_watercolor_canvas(img):
    import cv2, numpy as np
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (800, int(img.shape[0] * 800 / img.shape[1])))
    smooth = cv2.bilateralFilter(img, d=15, sigmaColor=100, sigmaSpace=100)
    Z = smooth.reshape((-1, 3))
    Z = np.float32(Z)
    K = 8
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 20, 1.0)
    _, label, center = cv2.kmeans(Z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    flat_colors = center[label.flatten()].reshape(smooth.shape)
    blurred = cv2.GaussianBlur(flat_colors, (15, 15), 0)
    watercolor = cv2.addWeighted(flat_colors, 0.7, blurred, 0.3, 0)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, 50, 150)
    edges = cv2.GaussianBlur(edges, (7, 7), 0)
    edges_color = cv2.cvtColor(255 - edges, cv2.COLOR_GRAY2BGR)
    watercolor = cv2.addWeighted(watercolor, 0.85, edges_color, 0.15, 0)
    hsv = cv2.cvtColor(watercolor, cv2.COLOR_BGR2HSV)
    hsv[:, :, 1] = np.clip(hsv[:, :, 1] * 1.25, 0, 255)
    hsv[:, :, 2] = np.clip(hsv[:, :, 2] * 1.05, 0, 255)
    watercolor = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    noise = np.random.normal(0, 10, watercolor.shape).astype(np.uint8)
    watercolor = cv2.addWeighted(watercolor, 0.95, noise, 0.05, 0)
    watercolor = cv2.GaussianBlur(watercolor, (5, 5), 1.2)
    watercolor = cv2.cvtColor(watercolor, cv2.COLOR_BGR2RGB)
    return watercolor

def apply_pop_art(img):
    import cv2, numpy as np
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    img = cv2.resize(img, (600, int(img.shape[0] * 600 / img.shape[1])))
    smooth = cv2.bilateralFilter(img, d=9, sigmaColor=100, sigmaSpace=100)
    gray = cv2.cvtColor(smooth, cv2.COLOR_BGR2GRAY)
    edges = cv2.adaptiveThreshold(
        gray, 255,
        cv2.ADAPTIVE_THRESH_MEAN_C,
        cv2.THRESH_BINARY,
        blockSize=9,
        C=9
    )
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    div = 64
    poster = img // div * div + div // 2
    pop = cv2.bitwise_and(poster, edges)
    hsv = cv2.cvtColor(pop, cv2.COLOR_BGR2HSV)
    hsv[..., 1] = np.clip(hsv[..., 1] * 2.2, 0, 255)
    hsv[..., 2] = np.clip(hsv[..., 2] * 1.2, 0, 255)
    pop = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    rows, cols, _ = pop.shape
    halftone = np.zeros((rows, cols), np.uint8)
    for y in range(0, rows, 8):
        for x in range(0, cols, 8):
            color_intensity = np.mean(pop[y:y+8, x:x+8])
            radius = int((255 - color_intensity) / 85)
            cv2.circle(halftone, (x, y), radius, 255, -1)
    halftone = cv2.cvtColor(halftone, cv2.COLOR_GRAY2BGR)
    pop = cv2.addWeighted(pop, 0.9, halftone, 0.1, 0)
    highlight = cv2.GaussianBlur(pop, (0, 0), 5)
    pop = cv2.addWeighted(pop, 1.2, highlight, -0.2, 0)
    return Image.fromarray(cv2.cvtColor(pop, cv2.COLOR_BGR2RGB))
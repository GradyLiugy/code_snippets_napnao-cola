import cv2
import os
import numpy as np


def remove_bright_areas(image, roi, threshold=150):
    """
    ȥ������Ȥ�����лҶ�ֵ�ϴ������

    :param image: ����ͼ�� (BGR)
    :param roi: ����Ȥ���� (x, y, width, height)
    :param threshold: �Ҷ���ֵ�����ڴ�ֵ�����ؽ����Ƴ�
    :return: ���˺��ͼ�������
    """
    # ��ȡ����Ȥ���� (ROI)
    roi_image = image[roi[1]:roi[3], :]

    # �� ROI ת��Ϊ�Ҷ�ͼ��
    gray_roi = cv2.cvtColor(roi_image, cv2.COLOR_BGR2GRAY)

    # �������룺�Ҷ�ֵ������ֵ��������Ϊ 1����ɫ����������ֵ��������Ϊ 0����ɫ��
    _, mask = cv2.threshold(gray_roi, threshold, 255, cv2.THRESH_BINARY_INV)

    # ʹ��������� ROI ͼ��
    filtered_roi = cv2.bitwise_and(roi_image, roi_image, mask=mask)
    cv2.imwrite(os.path.join(out_path, f'{ori_image.split("/")[-1].split(".")[0]}_filtered_roi.jpg'), filtered_roi)

    return filtered_roi, mask


def bgr_to_primary_color(image, mask):
    """
    ���� BGR ֵ�ж���Ҫ��ɫ���졢�̡�������

    :param bgr: ƽ����ɫ (B, G, R)
    :return: ��Ҫ��ɫ����
    """
    avg_color_per_row = cv2.mean(image, mask=mask)
    b, g, r = avg_color_per_row[:3]  # ���� alpha ͨ��������У�

    # ����һ���򵥵Ĺ������ж���ԭɫ
    if max(b, g, r) == r and r > g and r > b:
        return "Red"
    elif max(b, g, r) == g and g > r and g > b:
        return "Green"
    elif max(b, g, r) == b and b > r and b > g:
        return "Blue"
    else:
        return "Unknown"


def eaxB501Arar(ori_image):
    img = cv2.imread(ori_image)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ʹ�ø�˹�˲�����ͼ�����ƽ������
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # ʹ�� Canny ���Ӽ���Ե
    edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
    cv2.imwrite(os.path.join(out_path, 'canny.jpg'), edges)

    kernel = np.ones((2, 2), np.uint8)

    # ���ͱ�Ե
    dilation = cv2.dilate(edges, kernel, iterations=1)
    cv2.imwrite(os.path.join(out_path, 'dilation.jpg'), edges)

    fft_img = fft_flt(dilation)[:, :, None].astype(np.uint8)

    contours, _ = cv2.findContours(fft_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    polygons = []
    polygon_image = img.copy()
    contour_areas = []
    for contour in contours:
        area = cv2.contourArea(contour)
        contour_areas.append(area)

        # ���ƶ����
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx_polygon = cv2.approxPolyDP(contour, epsilon, True)

        # ֻ�����պϵĶ����
        if len(approx_polygon) > 5:
            polygons.append(approx_polygon)

            # ���ƶ��������
            cv2.drawContours(polygon_image, [approx_polygon], -1, (0, 0, 255), 2)

            cv2.imwrite(os.path.join(out_path, f'polygon.jpg'), polygon_image)


def fft_flt(img):
    f = np.fft.fft2(img)
    fshift = np.fft.fftshift(f)  # �ƶ���Ƶ����������

    # ��ȡƵ�׵���״
    rows, cols = image.shape[:2]
    crow, ccol = rows // 2, cols // 2

    # ����һ����ģ����������Ƶ�����ĸ����ĵ�Ƶ����
    mask = np.ones((rows, cols), dtype=np.uint8)

    # ��ֵ���ã�����Ƶ���еĸ�Ƶ���֣��˳���Ƶ����
    # ����һ����Χ������Ƶ���е�ˮƽ�ʹ�ֱƵ�ʷ���
    radius = 30  # �ɵ��ڰ뾶��ԽСԽ��ȥ�������Ƶ��Ϣ
    mask[crow - radius:crow + radius, :] = 0  # ˮƽ�ߣ�ȥ�����ĵĵ�Ƶ���֣�
    mask[:, ccol - radius:ccol + radius] = 0  # ��ֱ�ߣ�ȥ�����ĵĵ�Ƶ���֣�

    # Ӧ����ģ
    fshift = fshift * mask

    # ������Ҷ�任���ָ�ͼ��
    f_ishift = np.fft.ifftshift(fshift)  # ����λ
    image_back = np.fft.ifft2(f_ishift)
    image_back = np.abs(image_back)
    cv2.imwrite(os.path.join(out_path, 'image_back.jpg'), image_back)
    return image_back


def center_threshold_binarization(image_path, sacle, ratio):
    # ��ȡͼ��
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not open or find the image!")
        return

    # ת��Ϊ�Ҷ�ͼ��
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # ��ȡͼ��ߴ�
    height, width = gray_image.shape[:2]

    # �������ĵ�����
    center_x, center_y = width // 2, height // 2

    # ��ȡ���ĵ�ĻҶ�ֵ��Ϊ��ֵ
    threshold_value = gray_image[center_y, center_x] - 25

    print(f"Center pixel value (threshold): {threshold_value}")

    # Ӧ�ö�ֵ������������Ƕ�ֵ��Ϊ�ڰ�ɫ����0��255
    _, binary_image = cv2.threshold(gray_image, threshold_value, 255, cv2.THRESH_BINARY)
    cv2.imwrite(os.path.join(out_path, 'binary_image.jpg'), binary_image)

    kernel = np.ones((5, 5), np.uint8)
    # ���ͱ�Ե
    dilation = cv2.dilate(binary_image, kernel, iterations=1)

    contours, _ = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    large_contours = [cnt for cnt in contours if cv2.contourArea(cnt) > 100]
    cv2.drawContours(image, large_contours, -1, (0, 0, 255), 2)

    for cnt in large_contours:
        # ������Ӿ���
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(image, (x-5, y-5), (x + w + 5, y + h + 5), (0, 255, 0), 2)  # ������ɫ��ֱ������
        cv2.imwrite(os.path.join(out_path, 'counter_image.jpg'), image)

        x1, y1, x2, y2 = x, y, x+w, y+h

        row = np.int(np.ceil(w/sacle))
        line = np.int(np.ceil(h/sacle))

        for i in range(row):
            for j in range(line):
                x_1 = x1 + i * sacle
                y_1 = y1 + j * sacle
                x_2 = x1 + (i+1)*sacle
                y_2 = y1 + (j+1)*sacle
                cut_img = binary_image[y_1:y_2, x_1:x_2]
                cv2.imwrite(os.path.join(out_path, f'cut_img_{i}_{j}.jpg'), cut_img)
                # �����ɫ���ص�����
                white_pixel_count = cv2.countNonZero(cut_img)

                # �����ܵ�������
                total_pixel_count = sacle*sacle

                # �жϰ�ɫ���صı����Ƿ������ֵ
                if white_pixel_count / total_pixel_count > ratio:
                    # ��ԭʼͼ���ϻ��Ʊ߿�
                    cv2.rectangle(image, (x_1, y_1), (x_2, y_2), (255, 255, 0), 2)

        cv2.imwrite(os.path.join(out_path, 'counter_boxes.jpg'), image)



if __name__ == "__main__":
    # ��ȡͼ��
    ori_image = '/data/hjx/B19/data/ink/CF-RML14_202412051724141128.jpg'
    image = cv2.imread(ori_image)
    out_path = "/data/hjx/B19/data/out"
    if not os.path.exists(out_path):
        os.makedirs(out_path)

    if image is None:
        print("Error: Could not open or find the image!")


    # eaxB501Arar(ori_image)
    center_threshold_binarization(ori_image, 40, 0.2)


    
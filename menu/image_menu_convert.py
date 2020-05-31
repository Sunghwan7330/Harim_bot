import cv2
from pdf2image import convert_from_path

class ImageMenuConvert():
    day_array = ['mom', 'tue', 'wen', 'thu', 'fri']
    output_file = '{}_{}_{}.jpg'

    name_lunch = 'lunch'

    def devide_menu(self, ori_path: str):
        """
        src = cv2.imread(ori_path)
        #dst = src.copy()
        dst = src[1500:1823, 480:1530]
        cv2.imwrite('out2.jpg', dst)
        2300 ~ 2730
        """
        res_path = "image_menu"
        src = cv2.imread(ori_path)

        xx = 480
        yy = 1500
        width = 1050
        height = yy + 323
        # lunch A menu
        for i in range(0,5):
            #print("({}:{}, {}:{})".format(yy, height, xx+(width * i),xx+(width * (i+1))))
            dst = src[yy:height, xx+(width * i):xx+(width * (i+1))]
            filename = self.output_file.format(self.day_array[i], "lunch", "a")
            cv2.imwrite('{}/{}'.format(res_path, filename), dst)

        xx = 480
        yy = 1823
        height = yy + 323
        #lunch B menu
        for i in range(0,5):
            #print("({}:{}, {}:{})".format(yy, height, xx+(width * i), xx+(width * (i+1))))
            dst = src[yy:height, xx + (width * i):xx + (width * (i + 1))]
            filename = self.output_file.format(self.day_array[i], "lunch", "b")
            cv2.imwrite('{}/{}'.format(res_path, filename), dst)


        xx = 480
        yy = 2300
        height = yy + 430
        # lunch salad menu
        for i in range(0, 5):
            #print("({}:{}, {}:{})".format(yy, height, xx + (width * i), xx + (width * (i + 1))))
            dst = src[yy:height, xx + (width * i):xx + (width * (i + 1))]
            filename = self.output_file.format(self.day_array[i], "lunch", "salad")
            cv2.imwrite('{}/{}'.format(res_path, filename), dst)


def main():
    output_filename = 'target.jpg'
    pages = convert_from_path('target.pdf', 500)
    for page in pages:
        page.save(output_filename, 'JPEG')

    converter = ImageMenuConvert()
    converter.devide_menu(output_filename)


if __name__ == "__main__":
    main()

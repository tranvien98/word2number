import os 
import sys
WORKING_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(WORKING_DIR, "../"))
from word2number import w2n
import re

# text = ['TỨC NGÀY MƯỜI BỐN TRĂM HAI MƯƠI HAI TỶ ĐÔ LA MỸ TĂNG BẢY PHẨY TÁM PHẦN TRĂM SO VỚI CÙNG KỲ NĂM TRƯỚC ĐẠT MỨC CAO NHẤT TRONG NĂM NĂM QUA']

text = ["Hai mươi lăm sự kiện gần một trăm bốn mươi nghìn tỷ đồng doanh thu của vi na miu cố gắng đạt tám mươi sáu nghìn tỷ đồng."
, "Một ly hôn vào năm hai nghìn không trăm mười chín khiến ông phải chia hai mươi lăm phần trăm cổ phần ưu đãi dành cho vợ cũ và vắc xin sởi bất ngờ tuy nhiên kể từ thời kỳ đỉnh cao đó tài sản sóng xô đã giảm năm mươi bảy tỷ u ét đê theo bờ lum bớt và trước việc làm sốc với tuần trước tài sản của liên xô đã giảm hai mươi ba phần trăm so với cùng kỳ năm trước sau cổ phiếu."
,"SẢN XUẤT KINH DOANH TRONG QUÝ MỘT NĂM TÔI NGAY CÓ XU HƯỚNG PHỤC HỒI TĂNG TRƯỞNG QUÝ MỘT NĂM NAY SO VỚI CÙNG KỲ NĂM TRƯỚC ĐẠT MỨC KHÁ NĂM PHẨY BA PHẦN TRĂM CAO HƠN TỐC ĐỘ TĂNG BỐN PHẨY HAI PHẦN TRĂM CỦA QUÝ MỘT NĂM MỐT PHẨY SÁU PHẦN TRĂM MỘT NĂM MƯƠI",
"BA VẬN ĐỘNG XUẤT NHẬP KHẨU HÀNG HÓA PHỤC HỒI MẠNH MẼ VỚI TỔNG KIM NGẠCH XUẤT NHẬP KHẨU HÀNG HÓA ƯỚC TÍNH ĐẠT SÁU PHẨY BA TỶ ĐÔ LA MỸ TĂNG BẢY PHẨY TÁM PHẦN TRĂM SO VỚI THÁNG TRƯỚC NGÀY MƯỜI BỐN PHẨY BẢY PHẦN TRĂM SO VỚI CÙNG KỲ NĂM TRƯỚC TÍNH TRONG QUÝ MỘT THÁNG MƯỜI HAI TỔNG KIM NGẠCH XUẤT NHẬP KHẨU HÀNG HÓA ƯỚC TÍNH ĐẠT MỘT TRĂM BẨY SÁU PHẨY BA TỶ ĐÔ LA MỸ TĂNG MƯỜI BỐN PHẨY BỐN",
"PHẦN TRĂM SO VỚI CÙNG KỲ NĂM TRƯỚC TRONG ĐÓ XUẤT KHẨU TĂNG MƯỜI HAI PHẨY CHÍN PHẦN TRĂM NHU CẦU TĂNG NĂM PHẨY CHÍN PHẦN TRĂM"
,"LẠM PHÁT ĐƯỢC KIỂM SOÁT CHỈ SỐ GIÁ TIÊU DÙNG TIVI ĐÍNH HÔN QUÝ MỘT NĂM MỘT CHÍN HAI PHẦN TRĂM SO VỚI CÙNG KỲ NĂM TRƯỚC BIỆN PHÁP CƠ BẢN TĂNG KHÔNG PHẨY TÁM PHẦN TRĂM ĐÂY LÀ KẾT QUẢ ĐÁNG GHI NHẬN SỰ CHỈ ĐẠO ĐIỀU HÀNH GIÁ CỦA CHÍNH PHỦ TRONG BỐI CẢNH NHIỀU QUỐC GIA TRÊN THẾ GIỚI ĐANG GÁNH CHỊU CƠN BÃO GIÁ CHƯA TỪNG CÓ CHỪNG VÀI CHỤC NĂM QUA"
,"THÌ CHÚNG TA NHÌN THẤY RẰNG LÀ CÁI TỐC ĐỘ TĂNG TRƯỞNG CỦA NGÀNH CÔNG NGHIỆP VÀ XÂY DỰNG ĐẠT MỘT PHẨY BA PHẦN TRĂM VÀ NÓ CHIẾM KHOẢNG BA BẢY PHẨY CHÍN PHẦN TRĂM"
,"SỐ SÁU PHẦN TRĂM MƯỜI LĂM PHẦN TRĂM"
,"CHÚNG TA CÓ HỢP ĐỒNG PHẢI DỰA TRÊN CHỈ SỐ MƯƠI"
,"I XÊ BẢY PHẦN TRĂM MƯỜI NĂM PHẨY SÁU PHẦN TRĂM"
,"MỘT TRĂM BA MƯƠI TÁM NGHÌN TỶ ĐỒNG SẼ ĐẾN HAI HAI ĐẾN BA NĂM TỚI"
,"MỘT TRĂM TÁM MƯƠI CHÍN NGHÌN TỶ ĐỒNG VÀ CUỐI NĂM HAI NGÀN KHÔNG TRĂM HAI MƯƠI MỐT CÓ BẢY MƯƠI BA PHẦN TRĂM TRONG SỐ NÀY TƯƠNG ĐƯƠNG LÀ MỘT TRĂM BA MƯƠI TÁM NGHÌN TỶ ĐỒNG"
,"TỨC NGÀY MƯỜI BỐN TRĂM HAI MƯƠI HAI TỶ ĐÔ LA MỸ TĂNG BẢY PHẨY TÁM PHẦN TRĂM SO VỚI CÙNG KỲ NĂM TRƯỚC ĐẠT MỨC CAO NHẤT TRONG NĂM NĂM QUA"
,"CỬA HÀNG À LÀ BỞI MỘT PHẨY SÁU PHẦN TRĂM VÀ HÀNG BÊ LÀ BẢY PHẦN TRĂM"
,"TĂNG NĂM PHẨY BỐN PHẦN TRĂM THEO QUÝ VÀ NĂM PHẨY BA PHẦN TRĂM VÀO NĂM"
,"VÀ TỔNG HỢP CỦA CÁC TRUNG TÂM THƯƠNG MẠI NÀY TĂNG BẢY PHẨY NĂM PHẦN TRĂM SO VỚI QUÝ TRƯỚC VÀ HAI PHẨY NĂM PHẦN TRĂM SO VỚI CÙNG KỲ NĂM HAI KHÔNG HAI MỐT ĐẠT MỘT TRĂM BỐN MƯƠI NĂM ĐỔI MỚI CHUYỂN MỤC ĐÍCH DÙ HÓA MỨC GIÁ NÀY CAO GẤP BỐN LẦN THUÊ NGOÀI TẦM KHOẢNG BA MƯƠI LĂM PHẨY NĂM"
,"KHỦNG HƠN NGHÌN TỶ ĐỒNG CỦA CÔNG TY CỔ PHẦN TAY LÀM THỊT"
,"NGÀN TỶ ĐỒNG CỦA CÔNG TY CỔ PHẦN TẬP ĐOÀN HẢI DƯƠNG VỚI TÀI SẢN THẾ CHẤP"
,"TỔNG DOANH THU NĂM HAI NGÀN KHÔNG TRĂM HAI MƯƠI CỦA CÁC DOANH NGHIỆP ĐẠT HƠN MƯỜI NĂM NGÀN NĂM TRĂM TỶ ĐỒNG TĂNG TRÊN HAI MƯƠI HAI PHẦN TRĂM SO VỚI NĂM HAI NGÀN KHÔNG TRĂM MƯỜI CHÍN TRONG ĐÓ CÁC DOANH NGHIỆP"
,"GIÁ TRỊ HÀNG HÓA PHỤC VỤ TẾT HAI NGÀN KHÔNG TRĂM HAI MƯƠI HAI TRÊN ĐỊA BÀN ĐẠT KHOẢNG BA MƯƠI CHÍN NGÀN TỶ ĐỒNG"
,"LINH HOẠT KIỂM SOÁT HIỆU QUẢ"
,"NẾU NGHI NGỜ LỘ CẦN LẬP TỨC LIÊN HỆ NGÂN HÀNG PHẢI ĐÓNG THUẾ VÀ KHÁC HẲN VỚI KHÁCH HÀNG CŨNG KHÔNG TỰ NHẬT CÁC THÔNG TIN NÀY THEO CÁI ĐƯỜNG LINH ĐÃ ĐƯỢC GỬI ĐẾN SỐ ĐIỆN THOẠI CỦA MÌNH"
,"TỪ THÁNG MƯỜI HAI KHÔNG MƯỜI TÁM THÁNG MƯỜI HAI"
,"CHO HÀNG TRĂM NGƯỜI VAY VỚI LÃI SUẤT TỪ MỘT TRĂM LẺ CHÍN MƯƠI PHẦN TRĂM ĐẾN BA TRĂM SÁU MƯƠI PHẦN TRĂM"
,"NGÀY HAI MƯƠI CHÍN TRĂM TÁM MƯƠI BA TRIỆU ĐỒNG CÙNG NHIỀU TÀI SẢN CÓ GIÁ TRỊ"
,"THEO ĐÓ THÌ NHÓM KHÁCH HÀNG ĐƯỢC GIẢM TÌNH CHUYÊN TRÊN NHÓM CÁC DOANH NGHIỆP CHẾ BIẾN BẢO QUẢN THỦY SẢN VÀ CÁC SẢN PHẨM THỦY SẢN CHẾ BIẾN BẢO QUẢN KHÔNG QUẢ LÀ CÁC DOANH NGHIỆP SẢN XUẤT KINH DOANH NGHIỆP XUẤT KHẨU NĂM HAI NGÀN KHÔNG TRĂM HAI MƯƠI TỶ"
,"GIẢM TIỀN ĐIỆN ĐÃ CÓ HƠN MƯỜI SÁU NGÀN NĂM TRĂM TỶ ĐỒNG"
,"TRĂM PHẦN TRĂM LÊN MỘT TRĂM SÁU MƯƠI HAI TỶ ĐỒNG DO PHẢI TRÍCH LẬP DỰ PHÒNG GIẢM GIÁ KHOẢN ĐẦU TƯ VÀO CỔ PHIẾU HAI CỦA CÔNG TY CỔ PHẦN NÔNG TRƯỜNG KHÁCH HÀNG"
,"SAU KHI TRỪ CHI PHÍ BÁN HÀNG QUẢN LÝ DOANH NGHIỆP ÉP LỜ XÊ LỖI DÒNG VỐN TRĂM SÁU MƯƠI LĂM TỶ ĐỒNG CÙNG KỲ NĂM TRƯỚC DOANH NGHIỆP CÒN LẠI BỐN MƯƠI BA TỶ ĐỒNG TẠI THỜI ĐIỂM KẾT THÚC VỚI TỔNG TÀI SẢN CỦA ÉP LỜ XÊ ĐẠT HƠN BA MƯƠI LĂM NGHÌN TỶ ĐỒNG VỐN CHỦ SỞ HỮU CỦA DOANH NGHIỆP CHỊU TỶ ĐỒNG TRONG HƠN HAI MƯƠI SÁU NGHÌN TỶ ĐỒNG NỢ PHẢI TRẢ ÉP LỜ XÊ E NỜ HƠN BẢY NGHÌN BA TRĂM TỶ ĐỒNG"
,"TĂNG THÊM GẦN MỘT NGHÌN HAI TRĂM TỶ ĐỒNG SO VỚI HỒI ĐẦU NĂM TRONG CÁC THÁNG ĐẦU NĂM ÉP LỜ XÊ ĐÃ PHÁT HÀNH TÁM TRĂM NĂM MƯƠI TỶ ĐỒNG TRÁI PHIẾU KHIẾN DƯ NỢ CỦA TẬP ĐOÀN TĂNG THÊM HIỆN TẠI MỘT SỐ NGÂN HÀNG ĐA CẤP TÍN DỤNG CHO ÉP LỜ XÊ HÀNG NGHÌN TỶ ĐỒNG NHƯ ANH CỦA XÊ VÊ ĐÃ THÔNG BÁO SẼ SỚM THU HỒI CÁC KHOẢN CHO VAY VỚI TẬP ĐOÀN NÀY SAU SỰ KIỆN ÔNG TRỊNH VĂN QUYẾT ĐỊNH KHỞI TỐ LÃNH ĐẠO"
,"HAY CẢI THIỆN ĐƯỢC MỨC TĂNG TRƯỞNG NĂM PHẦN TRĂM CỦA UY VỪA QUA TRONG NĂM NAY KÉM PHÂN TÍCH DỰ BÁO CHIA SẺ VỀ CỦA VIỆT NAM TĂNG TRƯỞNG BẢY PHẨY MỘT PHẦN TRĂM SO VỚI CÙNG KỲ NHỮNG YẾU TỐ HỖ TRỢ KINH TẾ TỪ NỀN THẤP TRONG QUÝ BA NĂM HAI NGHÌN KHÔNG TRĂM HAI MƯƠI MỐT PÊ"
,"KHOẢNG MƯỜI CHÍN PHẨY BỐN PHẦN TRĂM TRONG NĂM HAI NGHÌN KHÔNG TRĂM HAI MƯƠI HAI TRONG KHI ĐÓ TRÊN SÀN HÁT NỜ ÍCH CHÍN MƯƠI MỐT DOANH NGHIỆP NIÊM YẾT ĐÃ CÔNG BỐ KẾ HOẠCH KINH DOANH CHO NĂM NAY DO ĐÓ CÁC DOANH NGHIỆP NÀY ĐẶT MỤC TIÊU TĂNG TRƯỞNG DOANH THU MƯỜI SÁU PHẨY TÁM PHẦN TRĂM VÀ LỢI NHUẬN SAU THUẾ TĂNG TRƯỞNG MƯỜI BA PHẨY BA PHẦN TRĂM CHO CẢ NĂM MỘT SỐ NGÀNH CÓ KẾ HOẠCH TĂNG TRƯỞNG LỢI NHUẬN CAO TRONG NĂM NAY BAO GỒM BÁN LẺ NGÂN"
,"TỔNG SỐ CỔ PHIẾU VÀ HAI MƯƠI PHẨY BẢY PHẦN TRĂM TỔNG VỐN HÓA TOÀN THỊ TRƯỜNG THEO ĐÓ TỔNG DOANH THU VÀ LỢI NHUẬN CỦA CÁC CÔNG TY NÀY LẦN LƯỢT BA MƯƠI MỐT PHẨY NĂM PHẦN TRĂM VÀ SÁU MƯƠI TÁM PHẨY MỘT PHẦN TRĂM SO VỚI CÙNG KỲ NĂM NGOÁI DO VỐN HÓA LỚN CÓ MỨC TĂNG TRƯỞNG LỢI NHUẬN CAO NHẤT LÀ NĂM MƯƠI MỐT PHẨY BA PHẦN TRĂM SO VỚI CÙNG KỲ VƯỢT TRỘI SO VỚI NHÓM NGÂN HÀNG TRUNG BÌNH VÀ NHÓM VỐN HÓA NHỎ CÓ MỨC TĂNG TRƯỞNG"
,"LỢI NHUẬN SONG LẦN LƯỢT LÀ BỐN MƯƠI LĂM PHẨY BỐN PHẦN TRĂM SO VỚI CÙNG KỲ VÀ HAI MƯƠI BA PHẨY BỐN PHẦN TRĂM SO VỚI CÙNG KỲ BỆNH CÓ TỈ LỆ DOANH NGHIỆP CÔNG BỐ BÁO CÁO KẾT QUẢ KINH DOANH QUỸ CAO HƠN BỐN MƯƠI PHẦN TRĂM THEO TỶ TRỌNG VỐN HÓA VÀ TẤT CẢ ĐỀU CÓ MỨC TĂNG TRƯỞNG LỢI NHUẬN KHÁCH QUAN TRONG SỐ BẢY NGÀY NAY HÓA CHẤT CÓ MỨC TĂNG TRƯỞNG LỢI NHUẬN SAU NGÀNH NHẤT LÀ NĂM PHẨY TÁM PHẦN TRĂM SO VỚI CÙNG"
,"KHI ĐÓNG GÓP HAI MƯƠI BẢY PHẦN TRĂM VÀ TĂNG TRƯỞNG LỢI NHUẬN SÓNG CỦA THỊ TRƯỜNG TRONG KHI ĐÓ CẢNH SÁT GIAO THÔNG ĐIỆN MỘT TRĂM LINH NĂM PHẨY NĂM PHẦN TRĂM SO VỚI CÙNG KỲ CÔNG NGHỆ VĂN SÁU PHẨY SÁU PHẦN TRĂM SO VỚI CÙNG KỲ DỊCH VỤ TÀI CHÍNH TĂNG HAI MƯƠI TÁM PHẨY CHÍN PHẦN TRĂM SO VỚI CÙNG KỲ HƯỚNG TĂNG HAI MƯƠI BẢY PHẨY HAI PHẦN TRĂM SO VỚI CÙNG KỲ SAU KHI GIA"
, "năm một chín hai mươi"
, "sáu phẩy ba tỷ dax sáu phẩy ba tỷ"
," năm hai nghìn không trăm mười chín"
]


for tx in text:
    # try:
    print(w2n(tx))
    # except:
    #     print(tx)


# print((convert))

# text = "một ba bảy chín"

# res = w2n_single(text)

# print(res)
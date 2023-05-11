### 0. Xuất mô hình từ Pytorch sang ONNX
  - Trong phần này, sẽ chuyển đổi một model sang ONNX
  - Hạn chế:
    - Mô hình là động, ví dụ như thay đổi hành vi tùy thuộc vào dữ liệu đầu vào, thì quá trình không chính xác.
  - Code ở: Pytorch_to_ONNX.ipynb
### 2. Cách sử dụng ONNX
  - Mọi phụ trợ ONNX phải hỗ trợ chạy mô hình ngay lập tức. Sau khi giải nén tarball của từng mô hình, sẽ có:
    - Tệp protobuf model.onnx đại diện cho mô hình ONNX được tuần tự hóa
    - Dữ liệu thử nghiệm ( ở dạng tệp TensorProto protobuf được tuần tự hóa hoặc kho lưu trữ Numpy được tuần tự hóa)
  - Code ở: Usega_ONNX.ipynb
### 3. Cách sử dụng - Kiểm tra mã khởi động dữ liệu
  - Sử dụng dữ liệu thử nghiệm từ mô hình ONNX từ Model Zoo.
  - Có 2 định dạng khác nhau cho các tệp dữ liệu thử nghiệm:
    - Protobuf được tuần tự hóa TensorProtos (.pb) được lưu trong các thư mục có quy ước đặt tên là test_data_set_*
    - Các kho lưu trữ Numpy được tuần tự hóa, được lưu trữ trong các tệp có quy ước đặt tên test_data_*.npz. Mỗi tệp chứa một bộ đầu vào và đầu ra thử nghiệm
  - Code: Trong ví dụ này, sẽ sử dụng model zoo là vgg16 - Code ở: Pre_trained_ONNX_model-zoo.ipynb
### 4. Tự build một Model bằng Pytorch và chuyển sang ONNX
  - Khi đặt cả hai model vào GPU, sau nhiều lần thử nghiệm thì thấy thời gian xử lý của ONNX nhanh hơn Pytorch
  - Trong ví dụ này: onnx gần như là nhanh tuyệt đối với 98/100
  - Code ở: Build_Model_to_ONNX.ipynb
### 5. Convert Faster-RCNN to ONNX
  - Model Faster-RCNN được lấy từ thư viện torchvision
  - Code ở: Faster-RCNN-ONNX.ipynb

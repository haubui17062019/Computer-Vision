### 0. Xuất mô hình từ Pytorch sang ONNX
  - Trong phần này, sẽ chuyển đổi một model sang ONNX
  - Hạn chế:
    - Mô hình là động, ví dụ như thay đổi hành vi tùy thuộc vào dữ liệu đầu vào, thì quá trình không chính xác.
  - Code ở: Pytorch_to_ONNX.ipynb
### 2. Cách sử dụng ONNX
  - Cách sử dụng model ONNX sau khi đã convert
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
### Bổ sung
Phần warn-up, em làm ở trong phần 7
### 6. Đánh đổi giữa hiệu suất và độ chính xác
  - Trong các chuyển đổi của model, tất cả đều dùng float32
  - Chuyển đổi mô hình sử dụng float16 có thể giảm kích thước mô hình (đến một nửa) và cải thiện hiệu suất trên một số GPU.
  - Khi chuyển đổi về float16 thì có thể mất mát về độ chính xác
### 7. Quantize model ONNX
  - Sử dụng model mobilenet_v2 
  - Chuyển đổi sang ONNX 
  - Load model float32 ở session_fp32
  - Sử dụng quantize_static được mô hình session_quant (từ fpt32 sang uint8)
  - So sánh kích thước: session_quant (3.5MB) nhẹ hơn session_fp32 (13.4MB) (khoảng 4 lần)
  - So sánh tốc độ: Có vẻ như là float32 nhanh hơn uint8
  - So sánh accuracy: fp32 có độ chính xác hơn uint8 (0.83 và 0.80)
  - Code ở: Quantize-ONNX.ipynb

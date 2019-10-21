1.字符级别的语言模型  
2.LSTM  三个门单元信息+记忆单元信息  
**Ct = Ct-1 * Forget + Ct' * Input**  
3.padding
3.1 mask矩阵,记录batch * max_length
3.2 实际句子长度,记录batch * length
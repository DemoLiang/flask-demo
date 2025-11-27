from unittest import TestCase
from app import sum1


class Test(TestCase):
    def test_sum1(self):
        # 测试场景1：当a > b时，函数应该返回a + b
        self.assertEqual(sum1(5, 3), 8, "当a > b时，应该返回a + b")
        # 测试场景2：当a < b时，函数应该返回a - b
        self.assertEqual(sum1(3, 5), -2, "当a < b时，应该返回a - b")
        
        # 测试场景3：当a = b时，函数应该返回a - b（因为a不大于b）
        self.assertEqual(sum1(4, 4), 0, "当a = b时，应该返回a - b")
        
        # 测试场景4：测试负数情况
        self.assertEqual(sum1(-1, -3), -4, "当a > b（都是负数）时，应该返回a + b")
        self.assertEqual(sum1(-3, -1), -2, "当a < b（都是负数）时，应该返回a - b")
        
        # 测试场景5：测试混合正负数情况
        self.assertEqual(sum1(5, -3), 2, "当a > b（a正b负）时，应该返回a + b")
        self.assertEqual(sum1(-3, 5), -8, "当a < b（a负b正）时，应该返回a - b")

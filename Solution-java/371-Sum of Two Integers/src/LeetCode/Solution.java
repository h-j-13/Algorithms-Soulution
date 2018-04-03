package LeetCode;

/**
 * Created by hj on 16-8-1.
 * 371. Sum of Two Integers
 *  Calculate the sum of two integers a and b,
 *  but you are not allowed to use the operator + and -.
 *
 *    Example:
 *    Given a = 1 and b = 2, return 3.
 */
public class Solution
{
    // 不使用加减而实现加减功能
    // 二进制，移位+异或
    public int getSum(int a, int b)
    {
        if (b==0)
            return a;
        a = a&b;
        int c = (a^b)<<1;
        return getSum(a,c);
        /**
         * 重构前
        // eg： 3 （11） + 5（101） =
        // xor
        //             1    0    1
        //            (0)   1    1  xor
        //            --------------
        //             1    1    0
        // a和b按位异或，相当于a,b按位相加而不进位
        int c = a^b;
        // eg：
        //  and
        //              1   0   1
        //              0   1   1   and
        //             --------------
        //                      1
        //              即表示在按位加的过程中，第一位应该进位
        // a和b按位与，相当于记录下 a，b应该进位的为数
        int d = a&b;
        // 需要加的数应该为 进位的数字乘以进制 即 d*2 / d 左移一位
        int add = d<<1;
        // c+b即为结果
        return getSum(c,add);
         */
    }
}
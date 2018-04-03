package Leetcode;

/**
 * Created by hj on 16-8-5.
 *
 */
public class Solution
{
    public int addDigits(int num)
    {
        return (num - 1) % 9 + 1;
        //num = abcde = (a+b+c+d+e)+(a*9999+b*999+c*99+d*9)
        //
        // 因为 a * 9999 + b * 999 + c * 99 + d * 9 一定可以被9整除，因此num模除9的结果与 a + b + c + d + e 模除9的结果是一样的。
        //
        //对数字 a + b + c + d + e 反复执行同类操作，最后的结果就是一个 1-9 的数字加上一串数字，
        //  最左边的数字是 1-9 之间的，右侧的数字永远都是可以被9整除的。
        //这道题最后的目标，就是不断将各位相加，相加到最后，当结果小于10时返回。因为最后结果在1-9之间，
        //  得到9之后将不会再对各位进行相加，因此不会出现结果为0的情况。因为 (x + y) % z = (x % z + y % z) % z，又因为 x % z % z = x % z，
        //  因此结果为 (num - 1) % 9 + 1，只模除9一次，并将模除后的结果加一返回。
        //先观察结果，然后在写简的算法
//        if(num<10)
//            return num;
//
//        int result = 0;
//        while(num!=0)
//        {
//            result += num%10;
//            num /= 10;
//        }
//        if(result < 10)
//            return result;
//        else
//            return addDigits(result);
    }
}

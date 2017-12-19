package LeetCode_344;

/**
 * Created by hj on 16-7-21.
 * LeetCode 344

 Write a function that takes a string as input and returns the string reversed.

 Example:
 Given s = "hello", return "olleh".
 */
public class Solution
{
    public String reverseString(String s)
    {
        //System.out.println(new StringBuffer(s).reverse().toString());
        //     返回一个新的 StringBuffer对象，参数为s，先倒序，在转换为字符串。
        return new StringBuffer(s).reverse().toString();
    }
}
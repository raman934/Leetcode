// Runtime : 4 ms
// Memory Usage : 9.1 MB
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2)
{
    struct ListNode* res = (struct ListNode*)malloc(sizeof(struct ListNode));
    struct ListNode* head = res;
    
    int carry = 0;
    int sum;

    while(l1 != NULL && l2 != NULL)
    {
        sum = l1->val + l2->val + carry;
        res->val = sum%10;
        carry = sum/10;
        l1 = l1->next;
        l2 = l2->next;
        printf("%d \n", res->val);
        if(l1 && l2)
        {
            res->next = (struct ListNode*)malloc(sizeof(struct ListNode));
            res = res->next;
        }
    }
    while(l1 == NULL && l2 != NULL)
    {
        res->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        res->next->val =(l2->val + carry)%10;
        carry = (l2->val + carry) / 10;
        res = res->next;
        l2 = l2->next;
    }
    while(l2 == NULL && l1 != NULL)
    {
        res->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        res->next->val =(l1->val + carry)%10;
        carry = (l1->val + carry) / 10;
        res = res->next;
        l1 = l1->next;
    }
    if(carry>0)
    {
        res->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        res->next->val = carry;
        res = res->next;
    }
    res->next = NULL;
    return head;
}

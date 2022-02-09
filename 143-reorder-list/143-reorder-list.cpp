/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    
    void printList(ListNode* head){
        auto temp = head;
        while(temp != nullptr){
            std::cout << temp->val << "->";
            temp = temp->next;
        }
        std::cout << std::endl;
    }
    
    size_t lenList(ListNode* head){
        auto temp = head;
        size_t len = 0;
        while(temp != nullptr){
            len++;
            temp = temp->next;
        }
        return len;
    }
    
    ListNode* reverseList(ListNode* head){
        ListNode* prev = nullptr;
        while(head != nullptr){
            auto temp = head->next;
            head->next = prev;
            prev = head;
            head = temp;
        }
        
        return prev;
    }
    
    ListNode* interleave(ListNode* head1, ListNode* head2){
        ListNode* res = new ListNode();
        auto temp = res;
        // head1 = 1 - 2 - 3 - *None, head2 = 6 - 5 - 4 _ *none, res = 0 - 1 - 6 - 2 - 5 - 3 - *4
        while(head1 != nullptr){
            res->next = head1; 
            head1 = head1->next;
            res = res->next;
            res->next = head2;
            head2 = head2->next;            
            res = res->next;
            // res = res->;
        }
        
        auto temp1 = temp->next;
        delete temp;
        return temp1;
    }
    
    void reorderList(ListNode* head) {
        /*
         create a even node reverse list
         traverse both and interleave alternate nodes
        
        traverse and add even nodes to end of one list and point odd nodes next pointer to the other next pointer
        */
        
        size_t len = lenList(head);
        if(len < 2){
            return;
        }
        size_t mid = len / 2;
        std::cout << mid << std::endl;
        auto temp = head;
        ListNode* prev = nullptr;
        while(mid--){
            prev = temp;
            temp = temp->next;
        }
        prev->next = nullptr;
        // printList(head);
        // printList(temp);
        
        auto reverseHead = reverseList(temp);
        // printList(reverseHead);
        
        auto res = interleave(head, reverseHead);
        // printList(head);
    }
};
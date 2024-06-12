typedef int TipoItem;
const int max_itens = 100;

class queue{
    private:
    int first, last;
    TipoItem* estrutura;

    public:
    queue();
    ~queue();
    bool isEmpty();
    bool isFull();
    void push(TipoItem item);
    TipoItem dequeue();
    void print();
};
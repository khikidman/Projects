#include <iostream>
#include <sstream>
#include <fstream>
using std::cout;
using std::cin;
using std::endl;
using std::array;
using std::vector;
using std::fstream;

time_t now = time(0);
tm* current_time = gmtime(&now);
tm* local_time = localtime(&now);

int time_diff = ((current_time->tm_yday) - (local_time->tm_yday)) * 24 + ((current_time->tm_hour) - (local_time->tm_hour));

class Task {
public:
    char* name;
    bool time_sensitive;
    bool completed;
    int recurring;
    tm* time;
};


class Event {
public:
    char* name;
    char* location;
    int recurring;
    tm* date;
};

class Calendar {
    
};

Task create_task(char* name, bool time_sensitive, tm* time){
    Task task;
    task.name = name;
    task.time_sensitive = time_sensitive;
    task.time = time;
    return task;
}

void get_calendar(int year, int month){

}

int main() {

    int year;
    int month;
    cin >> year >> month;
    // get_calendar(year, month);
    // cout << time_diff;
}
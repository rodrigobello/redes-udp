#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <ctype.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <netinet/in.h>

#define PORT 9909
#define MAXLINE 1024

int create_socket();
void setup_sockaddr_in(struct sockaddr_in (*), struct sockaddr_in (*));
void bind_address(struct sockaddr_in (*), int);
void send_response(int, char (*), int, struct sockaddr_in (*));


int main(int argc, char *argv[]) {
    int sockfd = create_socket();
    char buffer[MAXLINE];
    char response[MAXLINE];
    struct sockaddr_in server_address, client_address;

    setup_sockaddr_in(&server_address, &client_address);

    bind_address(&server_address, sockfd);

    // Receive message
    unsigned int len, n;
    n = recvfrom(sockfd, (char *)buffer, MAXLINE,
                MSG_WAITALL, ( struct sockaddr *) &client_address,
                &len);
    buffer[n] = '\0';

    char flag = buffer[0];

    for (int i=0;i<n;i++) {
        buffer[i] = buffer[i+1];
    }

    switch(flag) {
        case 'i':
        printf("Received the integer '%s' from client\n", buffer);
        int i = atoi(buffer);
        sprintf(response, "%d", i+1);
        break;

        case 's':
        break;

        case 'c':
        if (buffer[0] == toupper(buffer[0]))
            response[0] = tolower(buffer[0]);
        else
            response[0] = toupper(buffer[0]);
        response[1] = '\0';
        break;

        default:
        printf("Invalid type!");
        break;
    }

    send_response(sockfd, response, len, &client_address);

    return 0;
}

int create_socket() {
    int sockfd;
    if ( (sockfd = socket(AF_INET, SOCK_DGRAM, 0)) < 0 ) {
        perror("Fail to create socket");
        exit(EXIT_FAILURE);
    }
    return sockfd;
}

void setup_sockaddr_in(struct sockaddr_in *server_address, struct sockaddr_in *client_address) {
    memset(server_address, 0, sizeof(*server_address));
    memset(client_address, 0, sizeof(*client_address));

    // Filling server information
    (*server_address).sin_family = AF_INET;
    (*server_address).sin_addr.s_addr = INADDR_ANY;
    (*server_address).sin_port = htons(PORT);
}

void bind_address(struct sockaddr_in *server_address, int sockfd) {
    if ( bind(sockfd, (const struct sockaddr *)server_address,
            sizeof(*server_address)) < 0 )
    {
        perror("Fail to bind address");
        exit(EXIT_FAILURE);
    }
}

void send_response(int sockfd, char* message, int len, struct sockaddr_in *client_address) {
    sendto(sockfd, (const char *) message, strlen(message),
           MSG_CONFIRM, (const struct sockaddr *)client_address,
           len);
    printf("'%s' sent.\n", message);
}

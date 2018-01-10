#pragma once
#include <SDL2/SDL.h>
class Map
{
    public:
        Map();
        Map(int width,int height):
        w(width),h(height){}
        Map(int width,int height,SDL_Renderer*);
        ~Map();

        int w,h;
        unsigned char* data;
        void Draw(SDL_Renderer* ren);
        void Update();
        static void init(SDL_Renderer* ren);


    protected:

    private:
        SDL_Texture* chars;
};


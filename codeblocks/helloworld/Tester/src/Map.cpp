#include "Map.h"
#include <SDL2/SDL.h>
#include <cstdlib>
#include <time.h>
#include <stdio.h>

Map::Map()
{
    //ctor
}

Map::Map(int width,int height,SDL_Renderer* ren){
    w = width;h=height;
    srand(time(NULL));
    data = new char*[w];
    for(int i = 0;i<w;i++){
        data[i] = new char[h];
    }
    for(int y=0;y<height;y++){
        for(int x=0;x<width;x++){
            data[x][y] = 0;//rand()
            printf("%d,", data[x][y]);
        }
    }
    printf("\n");
    SDL_Surface* sur = SDL_LoadBMP("pics/chars.bmp");
    SDL_SetColorKey(sur,SDL_TRUE,SDL_MapRGB(sur->format,255,0,255));
    chars = SDL_CreateTextureFromSurface(ren,sur);
}


void Map::Update(){
}
void Map::Draw(SDL_Renderer* ren){
    for(int x=0;x<w;x++){
        for(int y=0;y<h;y++){
            int c = (int)data[x][y];
            SDL_Rect s;
            s.x = c*16;s.y = 0;
            s.w = 16;s.h = 16;
            SDL_Rect d;
            d.x = x*16;d.y = y*16;
            d.w = 16;d.h = 16;
            SDL_RenderCopy(ren,chars,&s,&d);
        }
    }
}

Map::~Map()
{
    //dtor
}

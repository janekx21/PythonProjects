#include <iostream>
#include <SDL2/SDL.h>
#include "Map.h"

int main(){
    SDL_Window* window = NULL;
    SDL_Renderer *ren = NULL;
    int mousex=0;
    int mousey=0;
    bool showrect = false;

    if(SDL_Init(SDL_INIT_VIDEO) < 0){
		printf("SDL error:%s\n",SDL_GetError() );
	}
	SDL_Surface* bitmap = SDL_LoadBMP("sprite.bmp");
	SDL_SetColorKey(bitmap,SDL_TRUE,SDL_MapRGB(bitmap->format,0,0,0));

	window = SDL_CreateWindow("windwo",100,100,200,200,SDL_WINDOW_SHOWN);
	ren = SDL_CreateRenderer(window,-1,SDL_RENDERER_ACCELERATED);
	SDL_Texture* tex = SDL_CreateTextureFromSurface(ren,bitmap);
    Map* map = new Map(16,16,ren);
    while(1) {
        SDL_Event e;
        SDL_GetMouseState(&mousex,&mousey);
        SDL_SetRenderDrawColor(ren,50,55,55,255);
        SDL_RenderClear(ren);
        SDL_SetRenderDrawColor(ren,255,255,0,255);
        if(SDL_PollEvent(&e)){
            if(e.type == SDL_QUIT){
                break;
            }
            if(e.type == SDL_KEYDOWN){
                SDL_Scancode key =e.key.keysym.scancode;
                if(key == SDL_SCANCODE_SPACE){
                    showrect = !showrect;
                }else if(key == SDL_SCANCODE_ESCAPE){
                    break;
                }
                else{
                    printf("key: %d\n",key);
                }
            }
        }
        SDL_RenderDrawLine(ren,0,0,mousex,mousey);
        /*
        if(showrect){
            SDL_Rect rect;
            rect.x = 10;
            rect.y = 10;
            rect.w = 100;
            rect.h = 100;
            SDL_RenderDrawRect(ren,&rect);
        }
        SDL_Rect souce;
        souce.x = 0;
        souce.y = 0;
        souce.w = 100;
        souce.h = 100;
        SDL_Rect dest;
        dest.x = 0;
        dest.y = 0;
        dest.w = 100;
        dest.h = 100;
        SDL_RenderCopy(ren,tex,&souce,&dest);
        */
        map->Draw(ren);
        SDL_RenderPresent(ren);
        //std::cout << "x:"<<mousex<<"y:"<<mousey << "\n";

        SDL_Delay(16);
    }
    SDL_DestroyRenderer(ren);
    SDL_DestroyWindow(window);
	SDL_Quit();
    return 0;
}

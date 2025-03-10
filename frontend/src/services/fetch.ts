import { serverConfig } from '@/server.config.ts'

export default class Fetch {
    public static async get<ResponseDTO>(endpoint: string): Promise<ResponseDTO> {
        const response = await fetch(serverConfig.baseURL + '/' + endpoint, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
        })

        return await response.json()
    }

    public static async post<RequestDTO, ResponseDTO>(endpoint: string, data: RequestDTO): Promise<ResponseDTO> {
        const response = await fetch(serverConfig.baseURL + endpoint, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(data),
        })

        return await response.json()
    }

    public static async put<RequestDTO, ResponseDTO>(endpoint: string, data: RequestDTO): Promise<ResponseDTO> {
        const response = await fetch(serverConfig.baseURL + endpoint, {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
            },
            body: JSON.stringify(data),
        })

        return await response.json()
    }
}

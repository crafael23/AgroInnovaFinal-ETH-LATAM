import { GqlOptionsFactory } from '@nestjs/graphql';
import { Injectable } from '@nestjs/common';
import { ApolloDriverConfig } from '@nestjs/apollo';
import { ApolloServerPluginLandingPageLocalDefault } from '@apollo/server/plugin/landingPage/default';

@Injectable()
export class GraphqlOptions implements GqlOptionsFactory {
  createGqlOptions(): Promise<ApolloDriverConfig> | ApolloDriverConfig {
    return {
      autoSchemaFile: true,
      playground: false,
      plugins: [ApolloServerPluginLandingPageLocalDefault()],
      subscriptions: {
        'graphql-ws': true,
      },
    };
  }
}
